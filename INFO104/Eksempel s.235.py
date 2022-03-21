def flytdiagram(n: int):
    s = 1
    while n > 0:
        s *= n
        print(f's *= n: {s}, {n}')
        n -= 1
        print(f'n -= 1: {n}')
    return s

print(flytdiagram(5))