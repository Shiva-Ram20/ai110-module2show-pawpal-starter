# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design
-> My initial UML design has 4 classes; Owner, Pet, Task & Schedule. Each class has several methods that stores and gets information. These classes work together to form the PawPal app.
- What classes did you include, and what responsibilities did you assign to each?
-> Owner: Stores owner information and a list of their pets. Provides methods to add, remove and update pet profiles
-> Pet: Stores individual pet details, links to the owner and manages a list of tasks and schedules
-> Task: Stores task details such as IDs, descriptions, due dates, recurrence for specific pets
-> Schedule: Manages the pet's tasks and handles filtering for daily, upcoming and overdue tasks

**b. Design changes**

- Did your design change during implementation?
-> Yes, I made around 5 design changes during implementation
- If yes, describe at least one change and why you made it.
-> One of the changes was adding a direct Schedule reference to the Pet class. Originally, Pet only hel a list of tasks, but adding a schedule attribute allowed the app to directly link generated daily plans to a specific pet profile.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
