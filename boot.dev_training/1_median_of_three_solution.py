def median_of_three(a, b, c):
    if a > b > c:
        return b
    elif b > a > c:
        return a
    else:
        return c
