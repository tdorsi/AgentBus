#!/usr/bin/env python3
"""Report coordination health for an AgentBus markdown workspace."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


TASK_RE = re.compile(r"^## (TASK-\d+):\s*(.+)$", re.MULTILINE)
MSG_RE = re.compile(r"^## (MSG-\d{8}-(?:[A-Z]+-)?[A-Z]?\d+)\s*$", re.MULTILINE)
EVENT_RE = re.compile(r"^## (EVENT-\d{8}-\d+)\s*$", re.MULTILINE)
DISPATCH_RE = re.compile(r"^## (DISPATCH-\d{8}-\d+)\s*$", re.MULTILINE)
DECISION_RE = re.compile(r"^## (DECISION-\d{8}-\d+)\s*$", re.MULTILINE)
FIELD_RE = re.compile(r"^(Status|Owner|From|To|Related Task|Created|Date):\s*(.*)$", re.MULTILINE)
BOARD_ROW_RE = re.compile(
    r"^\|\s*(TASK-\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|$",
    re.MULTILINE,
)
RETIRED_WATCHER_INBOX_RE = re.compile(r"comms[\\/]+inbox_watcher\.md")
HISTORY_CONTEXT_RE = re.compile(
    r"\b(retired|history|historical|archive|archived|legacy|source:|correction|corrected|replace|replaces|replaced)\b",
    re.IGNORECASE,
)


@dataclass
class Task:
    task_id: str
    title: str
    status: str
    owner: str
    source: Path


@dataclass
class Message:
    message_id: str
    sender: str
    recipient: str
    related_task: str
    status: str
    created: str
    needs_response: bool
    source: Path


@dataclass
class Decision:
    decision_id: str
    date: str
    owner: str
    related_task: str
    status: str
    source: Path


@dataclass
class IdOccurrence:
    identifier: str
    source: Path
    line: int


@dataclass
class BoardRow:
    task_id: str
    status: str
    owner: str
    reviewer: str
    source: str


@dataclass
class BoardDivergence:
    task_id: str
    field: str
    board_value: str
    task_value: str
    board_source: str
    task_source: Path


@dataclass
class InboxReference:
    source: Path
    line: int
    text: str


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def split_sections(text: str, pattern: re.Pattern[str]) -> list[tuple[re.Match[str], str]]:
    matches = list(pattern.finditer(text))
    sections: list[tuple[re.Match[str], str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections.append((match, text[match.end() : end]))
    return sections


def fields(section: str) -> dict[str, str]:
    return {match.group(1): match.group(2).strip() for match in FIELD_RE.finditer(section)}


def parse_tasks(root: Path) -> list[Task]:
    tasks: list[Task] = []
    for path in sorted((root / "tasks").glob("*.md")):
        if path.name == "task_template.md":
            continue
        text = read_text(path)
        for match, body in split_sections(text, TASK_RE):
            meta = fields(body)
            tasks.append(
                Task(
                    task_id=match.group(1),
                    title=match.group(2).strip(),
                    status=meta.get("Status", "Unknown"),
                    owner=meta.get("Owner", "Unassigned"),
                    source=path.relative_to(root),
                )
            )
    return tasks


def merge_tasks(tasks: list[Task]) -> list[Task]:
    source_priority = {
        Path("tasks/done.md"): 5,
        Path("tasks/review.md"): 4,
        Path("tasks/blocked.md"): 3,
        Path("tasks/active.md"): 2,
        Path("tasks/backlog.md"): 1,
    }
    merged: dict[str, Task] = {}
    for task in tasks:
        current = merged.get(task.task_id)
        if current is None:
            merged[task.task_id] = task
            continue
        task_priority = source_priority.get(task.source, 0)
        current_priority = source_priority.get(current.source, 0)
        if task_priority >= current_priority:
            merged[task.task_id] = task
    return sorted(merged.values(), key=lambda item: item.task_id)


def response_body(section: str) -> str:
    marker = "### Response"
    if marker not in section:
        return ""
    return section.split(marker, 1)[1].strip()


def parse_messages(root: Path) -> list[Message]:
    messages: list[Message] = []
    paths = list((root / "comms").glob("*.md")) + list((root / "comms" / "watcher_inbox").glob("*.md"))
    for path in sorted(paths):
        if path.name in {"message_template.md", "README.md"}:
            continue
        text = read_text(path)
        for match, body in split_sections(text, MSG_RE):
            meta = fields(body)
            status = meta.get("Status", "Info")
            needs_response = status in {"Request", "Blocker", "Review Needed"} and not response_body(body)
            messages.append(
                Message(
                    message_id=match.group(1),
                    sender=meta.get("From", "Unknown"),
                    recipient=meta.get("To", "Unknown"),
                    related_task=meta.get("Related Task", ""),
                    status=status,
                    created=meta.get("Created", ""),
                    needs_response=needs_response,
                    source=path.relative_to(root),
                )
            )
    return messages


def parse_decisions(root: Path) -> list[Decision]:
    text = read_text(root / "decisions" / "decision_log.md")
    decisions: list[Decision] = []
    for match, body in split_sections(text, DECISION_RE):
        meta = fields(body)
        decisions.append(
            Decision(
                decision_id=match.group(1),
                date=meta.get("Date", ""),
                owner=meta.get("Owner", ""),
                related_task=meta.get("Related Task", ""),
                status=meta.get("Status", ""),
                source=Path("decisions/decision_log.md"),
            )
        )
    return decisions


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def parse_ids(root: Path) -> list[IdOccurrence]:
    occurrences: list[IdOccurrence] = []
    search_paths = [
        ((root / "comms").glob("*.md"), MSG_RE),
        ((root / "comms" / "watcher_inbox").glob("*.md"), MSG_RE),
        ((root / "watcher").glob("*.md"), EVENT_RE),
        ((root / "watcher").glob("*.md"), DISPATCH_RE),
    ]
    for paths, pattern in search_paths:
        for path in sorted(paths):
            text = read_text(path)
            for match in pattern.finditer(text):
                occurrences.append(
                    IdOccurrence(
                        identifier=match.group(1),
                        source=path.relative_to(root),
                        line=line_number(text, match.start()),
                    )
                )
    return occurrences


def duplicate_ids(occurrences: list[IdOccurrence]) -> dict[str, list[IdOccurrence]]:
    grouped: dict[str, list[IdOccurrence]] = {}
    for occurrence in occurrences:
        grouped.setdefault(occurrence.identifier, []).append(occurrence)
    return {identifier: items for identifier, items in grouped.items() if len(items) > 1}


def parse_board(root: Path) -> dict[str, BoardRow]:
    text = read_text(root / "state" / "sprint_board.md")
    summary = text.split("\n## ", 1)[0]
    rows: dict[str, BoardRow] = {}
    for match in BOARD_ROW_RE.finditer(summary):
        task_id = match.group(1)
        if task_id == "Task":
            continue
        rows[task_id] = BoardRow(
            task_id=task_id,
            status=match.group(2).strip(),
            owner=match.group(3).strip(),
            reviewer=match.group(4).strip(),
            source=match.group(5).strip(),
        )
    return rows


def normalize_status(status: str) -> str:
    value = status.lower()
    if "dropped" in value:
        return "dropped"
    if "blocked" in value:
        return "blocked"
    if "done" in value or "accepted" in value or "complete" in value:
        return "done"
    if "changes requested" in value or "review" in value:
        return "review"
    if "active" in value or "progress" in value or "claimed" in value:
        return "active"
    if "dispatched" in value:
        return "dispatched"
    if "ready" in value:
        return "ready"
    if "backlog" in value:
        return "backlog"
    return value.strip()


def normalize_person(value: str) -> str:
    return " ".join(value.lower().split())


def board_divergences(tasks: list[Task], board: dict[str, BoardRow]) -> list[BoardDivergence]:
    divergences: list[BoardDivergence] = []
    task_by_id = {task.task_id: task for task in tasks}
    for task_id, task in task_by_id.items():
        row = board.get(task_id)
        if row is None:
            divergences.append(
                BoardDivergence(task_id, "presence", "missing from board", "present in tasks", "", task.source)
            )
            continue
        if normalize_status(row.status) != normalize_status(task.status):
            divergences.append(
                BoardDivergence(task_id, "status", row.status, task.status, row.source, task.source)
            )
        if normalize_person(row.owner) != normalize_person(task.owner):
            divergences.append(BoardDivergence(task_id, "owner", row.owner, task.owner, row.source, task.source))

    for task_id, row in board.items():
        if task_id not in task_by_id:
            divergences.append(
                BoardDivergence(task_id, "presence", "present on board", "missing from tasks", row.source, Path(""))
            )
    return divergences


def active_inbox_reference_files(root: Path) -> list[Path]:
    relative_paths = [
        "README.md",
        "agent_rules.md",
        "GEMINI.md",
        "procedures/agent_startup.md",
        "procedures/branching_strategy.md",
        "procedures/review_response.md",
        "watcher/watcher_rules.md",
        "watcher/watcher_seed_prompt.md",
        "watcher/routing_table.md",
        "watcher/dispatch_queue.md",
    ]
    return [root / relative for relative in relative_paths]


def active_inbox_references(root: Path) -> list[InboxReference]:
    references: list[InboxReference] = []
    for path in active_inbox_reference_files(root):
        text = read_text(path)
        for index, line in enumerate(text.splitlines(), start=1):
            if not RETIRED_WATCHER_INBOX_RE.search(line):
                continue
            if HISTORY_CONTEXT_RE.search(line):
                continue
            references.append(InboxReference(path.relative_to(root), index, line.strip()))
    return references


def key_files(root: Path) -> list[Path]:
    relative_paths = [
        "sprint.md",
        "roles.md",
        "tasks/backlog.md",
        "tasks/active.md",
        "tasks/blocked.md",
        "tasks/review.md",
        "tasks/done.md",
        "comms/broadcast.md",
        "comms/inbox_codex.md",
        "comms/inbox_claude.md",
        "comms/inbox_local_agent.md",
        "comms/watcher_inbox/codex.md",
        "comms/watcher_inbox/claude.md",
        "comms/watcher_inbox/gemini.md",
        "comms/watcher_inbox/quill.md",
        "decisions/decision_log.md",
    ]
    return [root / relative for relative in relative_paths]


def format_mtime(path: Path) -> str:
    if not path.exists():
        return "missing"
    return datetime.fromtimestamp(path.stat().st_mtime).strftime("%Y-%m-%d %H:%M")


def print_task_section(title: str, tasks: list[Task]) -> None:
    print(f"\n{title}")
    if not tasks:
        print("  None")
        return
    for task in tasks:
        print(f"  {task.task_id}: {task.title}")
        print(f"    Status: {task.status} | Owner: {task.owner} | Source: {task.source}")


def print_message_section(messages: list[Message]) -> None:
    print("\nMessages Needing Response")
    pending = [message for message in messages if message.needs_response]
    if not pending:
        print("  None")
        return
    for message in pending:
        print(f"  {message.message_id}: {message.status} from {message.sender} to {message.recipient}")
        print(f"    Related Task: {message.related_task or 'None'} | Source: {message.source}")


def print_decision_section(decisions: list[Decision], limit: int) -> None:
    print("\nRecent Decisions")
    if not decisions:
        print("  None")
        return
    for decision in decisions[-limit:]:
        print(f"  {decision.decision_id}: {decision.status}")
        print(f"    Date: {decision.date} | Owner: {decision.owner} | Task: {decision.related_task}")


def print_duplicate_id_section(duplicates: dict[str, list[IdOccurrence]]) -> None:
    print("\nDuplicate IDs")
    if not duplicates:
        print("  None")
        return
    for identifier, occurrences in sorted(duplicates.items()):
        print(f"  {identifier}")
        for occurrence in occurrences:
            print(f"    {occurrence.source}:{occurrence.line}")


def print_board_divergence_section(divergences: list[BoardDivergence]) -> None:
    print("\nBoard Divergences")
    if not divergences:
        print("  None")
        return
    for divergence in divergences:
        print(f"  {divergence.task_id}: {divergence.field}")
        task_source = divergence.task_source if str(divergence.task_source) else "tasks/*"
        print(f"    Board: {divergence.board_value} ({divergence.board_source or 'state/sprint_board.md'})")
        print(f"    Tasks: {divergence.task_value} ({task_source})")


def print_inbox_reference_section(references: list[InboxReference]) -> None:
    print("\nActive Retired-Inbox References")
    if not references:
        print("  None")
        return
    for reference in references:
        print(f"  {reference.source}:{reference.line}")
        print(f"    {reference.text}")


def print_update_section(root: Path) -> None:
    print("\nLast Update Timing")
    for path in key_files(root):
        print(f"  {path.relative_to(root)}: {format_mtime(path)}")


def run(root: Path, recent_decisions: int) -> int:
    root = root.resolve()
    if not (root / "agent_rules.md").exists() or not (root / "tasks").exists():
        print(f"Not an AgentBus workspace: {root}")
        return 2

    tasks = merge_tasks(parse_tasks(root))
    messages = parse_messages(root)
    decisions = parse_decisions(root)
    duplicates = duplicate_ids(parse_ids(root))
    divergences = board_divergences(tasks, parse_board(root))
    inbox_references = active_inbox_references(root)

    active_tasks = [task for task in tasks if "active" in task.status.lower()]
    blocked_tasks = [task for task in tasks if "blocked" in task.status.lower()]

    print("AgentBus Health Check")
    print(f"Workspace: {root}")
    print(f"Tasks: {len(tasks)} | Active: {len(active_tasks)} | Blocked: {len(blocked_tasks)}")
    print(f"Messages: {len(messages)} | Need Response: {sum(1 for msg in messages if msg.needs_response)}")
    print(f"Decisions: {len(decisions)}")
    print(
        f"Duplicate IDs: {len(duplicates)} | Board Divergences: {len(divergences)} | "
        f"Active Retired-Inbox References: {len(inbox_references)}"
    )

    print_task_section("Active Tasks", active_tasks)
    print_task_section("Blocked Tasks", blocked_tasks)
    print_message_section(messages)
    print_duplicate_id_section(duplicates)
    print_board_divergence_section(divergences)
    print_inbox_reference_section(inbox_references)
    print_decision_section(decisions, recent_decisions)
    print_update_section(root)

    has_issue = (
        blocked_tasks
        or any(message.needs_response for message in messages)
        or duplicates
        or divergences
        or inbox_references
    )
    return 1 if has_issue else 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Report AgentBus coordination health.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent,
        help="Path to the AgentBus workspace. Defaults to this script's directory.",
    )
    parser.add_argument(
        "--recent-decisions",
        type=int,
        default=5,
        help="Number of recent decisions to show.",
    )
    args = parser.parse_args()
    return run(args.root, args.recent_decisions)


if __name__ == "__main__":
    raise SystemExit(main())
