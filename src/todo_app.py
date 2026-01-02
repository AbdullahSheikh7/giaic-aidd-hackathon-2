from datetime import datetime
from typing import List, Optional
import json


class Task:
    """Represents a single todo task."""

    def __init__(self, task_id: int, title: str, description: str = "", completed: bool = False):
        self.id = task_id
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        """Convert task to dictionary for serialization."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    def __str__(self):
        status = "✓" if self.completed else "○"
        return f"[{status}] {self.id}: {self.title} - {self.description}"


class TodoApp:
    """Main todo application class with in-memory storage."""

    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """Add a new task to the todo list."""
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")

        task = Task(
            task_id=self.next_id,
            title=title.strip(),
            description=description.strip()
        )
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        """Get all tasks in the todo list."""
        return self.tasks

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """Get a task by its ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """Update a task's details."""
        task = self.get_task_by_id(task_id)
        if task:
            if title is not None:
                if title.strip():
                    task.title = title.strip()
                else:
                    raise ValueError("Task title cannot be empty")
            if description is not None:
                task.description = description.strip()
            task.updated_at = datetime.now()
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by its ID."""
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def mark_task_complete(self, task_id: int, completed: bool = True) -> bool:
        """Mark a task as complete or incomplete."""
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = completed
            task.updated_at = datetime.now()
            return True
        return False

    def mark_task_incomplete(self, task_id: int) -> bool:
        """Mark a task as incomplete."""
        return self.mark_task_complete(task_id, False)