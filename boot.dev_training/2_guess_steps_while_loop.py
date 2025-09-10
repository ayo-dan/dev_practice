def guess_steps(secret, start):
    steps = 0
    while start != secret:
        if start < secret:
            start += 1
            steps += 1
        else:
            start -= 1
            steps += 1
    return steps
