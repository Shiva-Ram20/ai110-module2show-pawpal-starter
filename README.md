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

# Run all of the tests
pytest -m pytest
```
Sample test output:
Test covers for sorting, recurrence & conflict detection along with filtering logic
```
collected 28 items                                                                                                                

ai110-module2show-pawpal-starter\tests\test_pawpal.py ............................                                          [100%]

======================================================= 28 passed in 0.06s =======================================================
```

-> Confidence Level: 5 Stars
High Confidence due to 100% test pass rate across all core scheduling algorithmns, boundary edge cases and invalid input checks.


## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting (by time or priority) | `Schedule.sort_by_priority()`, `Schedule.sort_by_time()` | `sort_by_priority()` ranks high > medium > low, with ties broken by the earlier `due_date`. `sort_by_time()` orders tasks chronologically by `scheduled_time`, pushing any unscheduled tasks to the end. Both are pure functions -- they return a new sorted list and accept an optional `tasks` list, defaulting to every task across the owner's pets, so the UI can sort a pool it already filtered without re-querying. |
| Non-blocking conflict warnings | `Schedule.check_for_conflicts()` (built on `Schedule.find_conflicts()`) | Compares every pair of tasks that have a `scheduled_time` assigned and flags any whose `[scheduled_time, scheduled_time + duration_minutes)` windows overlap. Conflicts are surfaced as ready-to-print warning strings (e.g. `"Conflict: 'Morning walk' (08:00 AM-08:30 AM) overlaps with 'Breakfast' (08:15 AM-08:25 AM)"`) rather than exceptions -- nothing is blocked, deleted, or auto-rescheduled, the owner just gets flagged and decides what to do. The check is also defensive: a malformed task is reported as its own warning line instead of crashing the whole check. |
| Single-pass filtering | `Schedule.filter_tasks(pet_id=None, status=None)` | Walks the owner's full task list exactly once in a single list comprehension, AND-ing the `pet_id` and `status` (`'completed'`, `'pending'`, `'overdue'`) predicates together per task rather than filtering by `pet_id` and then filtering that result by `status` in two separate passes. Passing `None` for either argument skips that check; an unrecognized `status` raises `ValueError` up front. |
| Daily/weekly task recurrence | `Task.mark_complete()` (via `Task.compute_next_occurrence()`) | Completing a one-off task (`recurrence is None`) just marks it done. Completing a `'daily'`/`'weekly'` task instead advances its `due_date` forward by the recurrence's interval (1 or 7 days, via Python's `timedelta`), clears `scheduled_time` so it gets re-planned, and leaves `is_completed` as `False` for that next occurrence -- so a recurring task never permanently "finishes," it just keeps rolling forward. |

## 📸 Demo Walkthrough

### Main UI features (`app.py`)

- **Owner info** -- name/email fields at the top, kept in `st.session_state` so they persist across reruns.
- **Pets** -- a form to add a pet (name, species, age) plus a dropdown to pick which pet you're currently managing tasks for.
- **Tasks for the selected pet** -- a form to add a task (title, duration, priority, due date/time) and a table of that pet's current tasks.
- **Today's Schedule** -- a "Generate schedule" button that calls `Schedule.generate_plan()` to assign `scheduled_time` to today's tasks, followed by:
  - Conflict warnings (`Schedule.check_for_conflicts()`) shown via `st.warning()` right at the top of the section.
  - A **Sort by** dropdown (Priority / Scheduled time) wired to `sort_by_priority()` / `sort_by_time()`.
  - **Filter by pet** (multiselect) and **Filter by status** (dropdown) controls wired to `filter_tasks()`.
  - Summary counters (`st.metric`) and a results table (`st.table`), with `st.success`/`st.info` reporting how many tasks matched.

### Example end-to-end workflow

1. **Add a pet.** Under "Pets," enter a name (e.g. "Biscuit"), pick a species, and click **Add pet**. A confirmation (`st.success`) appears and the pet becomes selectable.
2. **Schedule tasks.** With "Biscuit" selected, add a few tasks for today -- e.g. "Morning walk" (30 min, high priority, 8:00 AM) and "Breakfast" (10 min, high priority, 8:15 AM). Each appears instantly in the pet's task table.
3. **Add a second pet** (e.g. "Mochi") with its own tasks, to see the schedule combine tasks across every pet the owner has.
4. **View today's schedule.** Click **Generate schedule**. This calls `generate_plan()`, which sorts today's incomplete tasks by priority and packs them back-to-back starting at midnight, assigning each a `scheduled_time`.
5. **Observe scheduler behaviors:**
   - If two tasks' assigned time windows overlap (as in the Morning walk/Breakfast example above), a `st.warning()` conflict banner appears immediately above the schedule -- without blocking the rest of the page from rendering.
   - Switching **Sort by** between "Priority" and "Scheduled time" re-orders the table live, without needing to regenerate the plan.
   - Using **Filter by pet** / **Filter by status** narrows the table (e.g. Mochi's pending tasks only) while the metrics update to reflect the filtered count.
   - Marking a daily/weekly recurring task complete rolls its due date forward to the next occurrence instead of removing it from the list.

### Key scheduler behaviors shown

- Priority-first greedy packing in `generate_plan()`.
- Non-blocking conflict detection surfaced as warnings, not errors.
- Single-pass combined pet/status filtering via `filter_tasks()`.
- Chronological vs. priority sorting via `sort_by_time()`/`sort_by_priority()`.
- Recurring tasks (`'daily'`/`'weekly'`) rolling forward on completion instead of disappearing.

### Sample CLI output

`main.py` builds a demo owner with two pets and a deliberately scrambled set of tasks (including one overdue and one already-completed task), then exercises the same `Schedule` methods the Streamlit UI calls. Running it from the project root:

```bash
python main.py
```

produces output like:

```
Today's Schedule -- Sunday, October 18, 2026
========================================================
08:00 AM  Morning walk         (Biscuit, 30 min) [priority: high  ] - pending
08:30 AM  Breakfast            (Biscuit, 10 min) [priority: high  ] - pending
10:00 AM  Nail trim            (Mochi, 15 min) [priority: low   ] - done
12:00 PM  Litter box cleaning  (Mochi, 10 min) [priority: medium] - pending
06:30 PM  Evening playtime     (Mochi, 15 min) [priority: low   ] - pending

All tasks (insertion order -- deliberately scrambled)
-----------------------------------------------------
  [high  ] due 2026-10-18 08:30 AM  (sched: unscheduled)  Breakfast                  (Biscuit) - pending
  [high  ] due 2026-10-18 08:00 AM  (sched: unscheduled)  Morning walk               (Biscuit) - pending
  [high  ] due 2026-10-17 09:00 AM  (sched: unscheduled)  Give heartworm medication  (Biscuit) - pending
  [low   ] due 2026-10-18 06:30 PM  (sched: unscheduled)  Evening playtime           (Mochi) - pending
  [medium] due 2026-10-18 12:00 PM  (sched: unscheduled)  Litter box cleaning        (Mochi) - pending
  [low   ] due 2026-10-18 10:00 AM  (sched: unscheduled)  Nail trim                  (Mochi) - done

sort_by_priority() -- highest priority first, ties by due_date
--------------------------------------------------------------
  [high  ] due 2026-10-17 09:00 AM  (sched: unscheduled)  Give heartworm medication  (Biscuit) - pending
  [high  ] due 2026-10-18 08:00 AM  (sched: unscheduled)  Morning walk               (Biscuit) - pending
  [high  ] due 2026-10-18 08:30 AM  (sched: unscheduled)  Breakfast                  (Biscuit) - pending
  [medium] due 2026-10-18 12:00 PM  (sched: unscheduled)  Litter box cleaning        (Mochi) - pending
  [low   ] due 2026-10-18 10:00 AM  (sched: unscheduled)  Nail trim                  (Mochi) - done
  [low   ] due 2026-10-18 06:30 PM  (sched: unscheduled)  Evening playtime           (Mochi) - pending

filter_tasks(pet_id='p1') -- Biscuit only
-----------------------------------------
  [high  ] due 2026-10-18 08:30 AM  (sched: unscheduled)  Breakfast                  (Biscuit) - pending
  [high  ] due 2026-10-18 08:00 AM  (sched: unscheduled)  Morning walk               (Biscuit) - pending
  [high  ] due 2026-10-17 09:00 AM  (sched: unscheduled)  Give heartworm medication  (Biscuit) - pending

filter_tasks(status='completed')
--------------------------------
  [low   ] due 2026-10-18 10:00 AM  (sched: unscheduled)  Nail trim                  (Mochi) - done

filter_tasks(pet_id='p2', status='pending') -- combined filter
--------------------------------------------------------------
  [low   ] due 2026-10-18 06:30 PM  (sched: unscheduled)  Evening playtime           (Mochi) - pending
  [medium] due 2026-10-18 12:00 PM  (sched: unscheduled)  Litter box cleaning        (Mochi) - pending

sort_by_time() -- chronological by scheduled_time
-------------------------------------------------
  [high  ] due 2026-10-18 08:00 AM  (sched: 08:00 AM)  Morning walk               (Biscuit) - pending
  [high  ] due 2026-10-18 08:30 AM  (sched: 08:15 AM)  Breakfast                  (Biscuit) - pending
  [medium] due 2026-10-18 12:00 PM  (sched: 12:00 PM)  Litter box cleaning        (Mochi) - pending
  [low   ] due 2026-10-18 06:30 PM  (sched: 06:30 PM)  Evening playtime           (Mochi) - pending
  [high  ] due 2026-10-17 09:00 AM  (sched: unscheduled)  Give heartworm medication  (Biscuit) - pending
  [low   ] due 2026-10-18 10:00 AM  (sched: unscheduled)  Nail trim                  (Mochi) - done

check_for_conflicts()
---------------------
  WARNING: Conflict: 'Morning walk' (08:00 AM-08:30 AM) overlaps with 'Breakfast' (08:15 AM-08:25 AM)
```

Note how `sort_by_time()` and `check_for_conflicts()` only "see" `t1`/`t2`/`t3`/`t4` because `main.py` hand-assigns overlapping `scheduled_time` values for the demo; `generate_plan()` itself always packs tasks back-to-back and never produces an overlap on its own.

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
