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
