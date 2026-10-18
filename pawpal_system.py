"""
PawPal+ core domain model.

Classes:
    Owner    - a pet owner and their contact info
    Pet      - a pet belonging to an Owner
    Task     - a single care task for a Pet (walk, feeding, meds, etc.)
    Schedule - organizes a Pet's Tasks into a daily plan

This module contains structure only (attributes + method stubs).
Scheduling/planning logic will be filled in during the next pass.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Task:
    """A single care task for a pet (e.g., walk, feeding, meds, grooming)."""

    task_id: str
    pet_id: str
    title: str
    description: str
    category: str  # e.g., "walk", "feeding", "meds", "grooming", "enrichment"
    duration_minutes: int
    priority: str  # e.g., "low", "medium", "high"
    due_date: datetime
    recurrence: Optional[str] = None  # e.g., "daily", "weekly", None for one-off
    is_completed: bool = False

    def mark_complete(self) -> None:
        raise NotImplementedError

    def mark_incomplete(self) -> None:
        raise NotImplementedError

    def is_overdue(self) -> bool:
        raise NotImplementedError

    def reschedule(self, new_date: datetime) -> None:
        raise NotImplementedError


@dataclass
class Pet:
    """A pet belonging to an Owner."""

    pet_id: str
    name: str
    species: str
    breed: str
    age: int
    owner_id: str
    weight: Optional[float] = None
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        raise NotImplementedError

    def remove_task(self, task_id: str) -> None:
        raise NotImplementedError

    def get_profile(self) -> dict:
        raise NotImplementedError

    def update_profile(self, **kwargs) -> None:
        raise NotImplementedError


class Owner:
    """A pet owner who manages one or more pets."""

    def __init__(
        self,
        owner_id: str,
        name: str,
        email: str,
        phone: str,
        pets: Optional[list[Pet]] = None,
    ) -> None:
        self.owner_id = owner_id
        self.name = name
        self.email = email
        self.phone = phone
        self.pets: list[Pet] = pets if pets is not None else []

    def add_pet(self, pet: Pet) -> None:
        raise NotImplementedError

    def remove_pet(self, pet_id: str) -> None:
        raise NotImplementedError

    def get_pets(self) -> list[Pet]:
        raise NotImplementedError

    def update_contact_info(self, email: Optional[str] = None, phone: Optional[str] = None) -> None:
        raise NotImplementedError


class Schedule:
    """Organizes a Pet's Tasks into a plan, applying constraints and priorities."""

    def __init__(self, schedule_id: str, pet_id: str, tasks: Optional[list[Task]] = None) -> None:
        self.schedule_id = schedule_id
        self.pet_id = pet_id
        self.tasks: list[Task] = tasks if tasks is not None else []

    def add_task(self, task: Task) -> None:
        raise NotImplementedError

    def remove_task(self, task_id: str) -> None:
        raise NotImplementedError

    def get_daily_tasks(self, date: datetime) -> list[Task]:
        raise NotImplementedError

    def get_upcoming_tasks(self, days: int = 7) -> list[Task]:
        raise NotImplementedError

    def get_overdue_tasks(self) -> list[Task]:
        raise NotImplementedError

    def generate_plan(self, available_minutes: Optional[int] = None) -> list[Task]:
        """Produce an ordered daily plan honoring time/priority constraints."""
        raise NotImplementedError
