# 01 — Python Fundamentals Practice

Three Colab-style practice notebooks with short, self-contained exercises. No external
dataset — each cell trains on small hand-written lists/dicts/strings defined inline.
These are drills on core Python mechanics (loops, functions, classes, lambdas), not
applied data-science work.

## Files

### `S2_Python_task (3).ipynb`
**Trained on:** small inline lists, strings, and numbers written directly in the cells
(no file/dataset).
**Problems being solved (one per cell):**
- Find the maximum value (and its index) in a list
- Count vowels in a user-input string
- Find all prime numbers within a range (sieve-by-trial-division)
- Generate a Fibonacci sequence up to N terms
- Simulate a basic ATM withdrawal (balance check)
- Find common elements between two lists
- Calculate the factorial of a number
- Validate user input against a stored key using a while loop
- Sum the digits of a number
- Draw a simple triangle pattern with nested loops
- Check whether a string is a palindrome
- Build a dictionary from two parallel lists
- Simulate a password check with a limited number of attempts
- Generate multiplication tables for a range of numbers

### `S3_Python (1).ipynb`
**Trained on:** small inline lists/strings (no file/dataset), used to practice `lambda`
functions specifically.
**Problems being solved (one per cell):**
- Average of a list of numbers (lambda)
- Longest word in a list of strings (lambda + `max(key=len)`)
- Prime-number check (lambda)
- Celsius-to-Fahrenheit conversion (lambda)
- List of squares via list comprehension inside a lambda
- Uppercase every string in a list (lambda)
- Total price including tax (lambda)
- Min/max of a list returned as a dict (lambda)
- Basic (naive) email-format validator (lambda)
- Character-frequency counter for a string (lambda with a nested closure)

### `S4_Python (1).ipynb`
**Trained on:** no external dataset — each cell defines and exercises a small class
in isolation. Focus is object-oriented design.
**Problems being solved (one class per cell):**
- `inventory` — add/remove items, track quantities in a dict
- `calculator` — basic arithmetic operations on a class, plus a playful "trick" method
- `student` — a simple student-record class (add/update/remove fields)
- `bank_account` — deposit/withdraw with balance checks
- `library` — add/remove books and track quantities
- `Tideman` — implementation of the Tideman (ranked-pairs) voting algorithm from CS50
- `temp_conv` — Celsius↔Fahrenheit conversion as a class
- `car_rent` — rental cost calculation from a daily rate and number of days

> Note: `S3_Python__1_.ipynb` and `S4_Python__1_.ipynb` appear twice among the uploads
> under slightly different filenames but are the same notebooks; only one copy of each
> is kept here.
