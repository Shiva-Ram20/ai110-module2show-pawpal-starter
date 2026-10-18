from datetime import datetime

from pawpal_system import Pet, Task


def make_task(task_id: str = "t1", pet_id: str = "p1") -> Task:
    return Task(
        task_id=task_id,
        pet_id=pet_id,
        title="Morning walk",
        description="30-minute walk around the block",
        category="walk",
        duration_minutes=30,
        priority="high",
        due_date=datetime(2026, 1, 1, 8, 0),
    )


def test_task_completion():
    task = make_task()
    assert task.is_completed is False

    task.mark_complete()

    assert task.is_completed is True


def test_task_addition():
    pet = Pet(
        pet_id="p1",
        name="Biscuit",
        species="dog",
        breed="Golden Retriever",
        age=3,
        owner_id="o1",
    )
    assert len(pet.tasks) == 0

    pet.add_task(make_task(task_id="t1", pet_id=pet.pet_id))

    assert len(pet.tasks) == 1
