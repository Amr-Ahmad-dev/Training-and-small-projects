# 02 — Student Management System (CLI)

### `assigment.py`
**Trained on:** no external dataset — data is entered live by the user through
`input()` prompts and stored in two in-memory dictionaries (`all_students`,
`all_courses`) for the duration of the program run.

**Problem being solved:** a terminal-based menu app for managing students and the
courses they take:
- Add a student (name, age, year, department) along with the courses they're taking
  and a numeric grade per course, converting each numeric grade to a letter grade
  via `grade_leter()`
- Add a new course to the course catalog
- List / look up an individual student's full record
- List / look up an individual course's record
- List students who passed vs. failed (grade threshold)
- List all students together with their computed letter grade
- Compute the class average grade
- Find the student with the highest and lowest grade
- A small unrelated `hallow_world()` greeting function, wired into the same menu

Everything runs through a `main()` loop that reads a numeric menu choice from the
user and dispatches to the matching function.
