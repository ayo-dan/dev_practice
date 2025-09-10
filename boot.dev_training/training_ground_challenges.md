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

# 3. Loop Stats: Sum, Count, Find

Complete the `compute_loop_stats(n, text, target)` function.  

Use **for loops** to compute three results and return them in a tuple, in this order:  

1. The sum of all integers from 1 to `n` (`0` if `n` is 0)  
2. How many times the character `target` appears in `text`  
3. The first index of `target` in `text` (0-based), or `-1` if it's not present  

---

### Constraints and Tips:
- Use a `for` loop with `range()` to sum numbers.  
- Use a `for` loop to count matches in the string.  
- Use `enumerate()` to find the first index.  
- Do not print anything from your function, just return the tuple `(sum_n, count, first_index)`.

---

### Examples
a = compute_loop_stats(5, "hello world", "l")

(15, 3, 2)
b = compute_loop_stats(0, "Boot.dev", "x")

(0, 0, -1)
