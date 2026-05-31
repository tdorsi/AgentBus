#!/usr/bin/env python3
"""Report coordination health for an AgentBus markdown workspace."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


TASK_RE = re.compile(r"^## (TASK-\d+):\s*(.+)$", re.MULTILINE)
MSG_RE = re.compile(r"^## (MSG-\d{8}-\d+)\s*$", re.MULTILINE)
DECISION_RE = re.compile(r"^## (DECISION-\d{8}-\d+)\s*$", re.MULTILINE)
FIELD_RE = re.compile(r"^(Status|Owner|From|To|Related Task|Created|Date):\s*(.*)$", re.MULTILINE)


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
    for path in sorted((root / "comms").glob("*.md")):
        if path.name == "message_template.md":
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

    active_tasks = [task for task in tasks if "active" in task.status.lower()]
    blocked_tasks = [task for task in tasks if "blocked" in task.status.lower()]

    print("AgentBus Health Check")
    print(f"Workspace: {root}")
    print(f"Tasks: {len(tasks)} | Active: {len(active_tasks)} | Blocked: {len(blocked_tasks)}")
    print(f"Messages: {len(messages)} | Need Response: {sum(1 for msg in messages if msg.needs_response)}")
    print(f"Decisions: {len(decisions)}")

    print_task_section("Active Tasks", active_tasks)
    print_task_section("Blocked Tasks", blocked_tasks)
    print_message_section(messages)
    print_decision_section(decisions, recent_decisions)
    print_update_section(root)

    return 1 if blocked_tasks or any(message.needs_response for message in messages) else 0


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
