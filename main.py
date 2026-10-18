"""Demo script: build an Owner with multiple pets/tasks and print today's schedule."""

from datetime import datetime

from pawpal_system import Owner, Pet, Task, Schedule


def build_demo_owner() -> Owner:
    owner = Owner(
        owner_id="o1",
        name="Jordan",
        email="jordan@example.com",
        phone="555-0100",
    )

    biscuit = Pet(
        pet_id="p1",
        name="Biscuit",
        species="dog",
        breed="Golden Retriever",
        age=3,
        owner_id=owner.owner_id,
    )
    mochi = Pet(
        pet_id="p2",
        name="Mochi",
        species="cat",
        breed="Tabby",
        age=2,
        owner_id=owner.owner_id,
    )
    owner.add_pet(biscuit)
    owner.add_pet(mochi)

    today = datetime.now().replace(second=0, microsecond=0)

    biscuit.add_task(
        Task(
            task_id="t1",
            pet_id=biscuit.pet_id,
            title="Morning walk",
            description="30-minute walk around the block",
            category="walk",
            duration_minutes=30,
            priority="high",
            due_date=today.replace(hour=8, minute=0),
        )
    )
    biscuit.add_task(
        Task(
            task_id="t2",
            pet_id=biscuit.pet_id,
            title="Breakfast",
            description="Morning feeding",
            category="feeding",
            duration_minutes=10,
            priority="high",
            due_date=today.replace(hour=8, minute=30),
        )
    )
    mochi.add_task(
        Task(
            task_id="t3",
            pet_id=mochi.pet_id,
            title="Litter box cleaning",
            description="Scoop and refresh litter",
            category="cleaning",
            duration_minutes=10,
            priority="medium",
            due_date=today.replace(hour=12, minute=0),
        )
    )
    mochi.add_task(
        Task(
            task_id="t4",
            pet_id=mochi.pet_id,
            title="Evening playtime",
            description="Interactive wand toy session",
            category="enrichment",
            duration_minutes=15,
            priority="low",
            due_date=today.replace(hour=18, minute=30),
        )
    )

    return owner


def print_schedule(owner: Owner) -> None:
    today = datetime.now()
    schedule = Schedule(schedule_id="s1", owner=owner)
    owner.schedule = schedule

    todays_tasks = sorted(schedule.get_daily_tasks(today), key=lambda t: t.due_date)

    print(f"Today's Schedule -- {today.strftime('%A, %B %d, %Y')}")
    print("=" * 56)

    if not todays_tasks:
        print("No tasks scheduled for today.")
        return

    for task in todays_tasks:
        pet_name = task.pet.name if task.pet else task.pet_id
        time_label = task.due_date.strftime("%I:%M %p")
        status = "done" if task.is_completed else "pending"
        print(
            f"{time_label}  {task.title:<20} ({pet_name}, {task.duration_minutes} min) "
            f"[priority: {task.priority:<6}] - {status}"
        )

    conflicts = schedule.find_conflicts()
    if conflicts:
        print("\nConflicts detected:")
        for first, second in conflicts:
            print(f"  - {first.title} overlaps with {second.title}")


if __name__ == "__main__":
    demo_owner = build_demo_owner()
    print_schedule(demo_owner)
