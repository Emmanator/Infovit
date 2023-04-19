def a_count(n):
    solutions = 0

    for a in range(n + 1):
        for b in range(n + 1):
            c = n - (a - b)
            if c >= 0:
                solutions += 1

    return solutions
