# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

### Implementation Summary

PawPal+ is built using an object-oriented Python architecture centered around four main classes:
- Owner: Manages a collection of pets and lists all pet tasks using 'get_all_tasks()'
- Pet: Holds individual pet profile data and a list of specific care tasks
- Task: Represents individual activities with metadata like duration, priority, due date and completion status
- Schedule: Acts as the system brain, retrieving a list of tasks from the Owner to filter, sort and organize care plans

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
Today's Schedule -- Sunday, October 18, 2026
========================================================
08:00 AM  Morning walk         (Biscuit, 30 min) [priority: high  ] - pending
08:30 AM  Breakfast            (Biscuit, 10 min) [priority: high  ] - pending
12:00 PM  Litter box cleaning  (Mochi, 10 min) [priority: medium] - pending
06:30 PM  Evening playtime     (Mochi, 15 min) [priority: low   ] - pending
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
# Paste your pytest output here
```

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Schedule.sort_by_priority()`, `Schedule.sort_by_time()` | `sort_by_priority()` ranks high > medium > low, with ties broken by the earlier `due_date`. `sort_by_time()` orders tasks chronologically by `scheduled_time`, pushing any unscheduled tasks to the end. Both accept an optional `tasks` list and default to every task across the owner's pets. |
| Filtering | `Schedule.filter_tasks(pet_id=None, status=None)` | Filters by `pet_id` and/or `status` (`'completed'`, `'pending'`, `'overdue'`); both filters are AND'd together, and passing `None` skips that check. Raises `ValueError` for an unrecognized `status`. |
| Conflict handling | `Schedule.check_for_conflicts()` (built on `Schedule.find_conflicts()`) | Compares every pair of tasks that have a `scheduled_time` assigned and flags any whose `[scheduled_time, scheduled_time + duration_minutes)` windows overlap. Returns ready-to-print warning strings (e.g. `"Conflict: 'Morning walk' (08:00 AM-08:30 AM) overlaps with 'Breakfast' (08:15 AM-08:25 AM)"`) and is defensive -- a malformed task is reported as its own warning instead of crashing the check. |
| Recurring tasks | `Task.mark_complete()` (via `Task.compute_next_occurrence()`) | Completing a one-off task just marks it done. Completing a `'daily'`/`'weekly'` task instead advances its `due_date` forward by the recurrence's interval (1 or 7 days, via Python's `timedelta`), clears `scheduled_time`, and leaves it pending for that next occurrence -- so it never truly "finishes." |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
