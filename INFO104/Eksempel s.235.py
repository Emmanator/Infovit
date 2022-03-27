def flytdiagram(n: int):
    s = 1
    while n > 0:
        s *= n
        print(f's *= n: {s}, {n}')
        n -= 1
        print(f'n -= 1: {n}')
    return s


def faktorial1(n):  # Rekursiv funksjon
    if n <= 1:
        return 1
    else:
        return faktorial1(n - 1) * n


a = faktorial1(10)
b = faktorial1(7)
print(a / b)
