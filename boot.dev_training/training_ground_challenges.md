# 1. Median of Three Challenge

Complete the `median_of_three(a, b, c)` function.

It should return the **median** (the middle value) of the three integer inputs using only comparisons and conditionals.

---

## Requirements

- **Do not use loops, lists, dictionaries, or sorting**
- **Use comparisons to determine which value is the middle**
- **Handle duplicates correctly** (e.g., `5, 5, 1` → `5`)

---

## Tips

- The median is the value that is **neither the minimum nor the maximum**.
- You can check if a value lies between the other two using **chained comparisons**.

---

## Examples
a, b, c = 3, 9, 5
print(median_of_three(a, b, c))

5
print(median_of_three(10, 2, 10))

10
print(median_of_three(-1, -5, -3))

-3

---

## Expected Behavior

- **Return exactly one of the inputs**, the one that is in the middle when sorted.
- **No printing from the function.**
- **No mutation of inputs.**

# 2. Guess Steps (While Loop)

Complete the `guess_steps` function.

### Problem Statement
Given two integers, `secret` and `start`, simulate a simple "guessing" process:

- Start from `start`
- While the current value is **not equal** to `secret`:
  - If it's less than `secret`, **increase it by 1**
  - If it's greater than `secret`, **decrease it by 1**
  - **Count how many steps** it takes to reach `secret`
- Return the step count

#### Requirements
- Use a `while` loop to move the value one step toward `secret` each iteration
- Use comparisons and an `if/else` to decide whether to increment or decrement
- If `start == secret`, return `0`

---

### Example Usage
print(guess_steps(10, 7))

Output: 3 # (7 -> 8 -> 9 -> 10)
print(guess_steps(-5, 2))

Output: 7 # (2 -> 1 -> 0 -> -1 -> -2 -> -3 -> -4 -> -5)

# 3. Fix Consecutive Run Compression

You're building a simple log compressor for a retro game. The `compress_runs` function should compress a list into counts of consecutive duplicates.

**Expected behavior:**  
Return a list of `[value, count]` pairs for each consecutive run.

### Examples
compress_runs([1, 1, 2, 2, 2, 3])
# [[1, 2], [2, 3], [3, 1]]

compress_runs(["a", "a", "a", "b", "b", "a"])
# [["a", 3], ["b", 2], ["a", 1]]

### What's Wrong Now

The buggy implementation counts all occurrences of a value in the entire list instead of counting only consecutive runs. This merges separate runs incorrectly and skips positions incorrectly.

### Your Task

- Iterate through the list once.
- Track the current value and how many times it repeats consecutively.
- When the value changes, append `[value, count]` to the result and reset the counter.
- Handle edge cases like empty lists and single-element lists.

**Notes:**
- Only use lists and loops. Don't use dictionaries or sets.
- Preserve the original order of runs.

