# Oppgave 1
def faktorial1(n):
    if n <= 1:
        return 1
    else:
        return faktorial1(n - 1) * n


def faktorial2(n):
    fak = 1
    for i in range(1, n + 1):
        fak *= i
    return fak


def faktorial3(n):
    fak = 1
    while n != 1:
        fak *= n
        n -= 1
    return fak

# Oppgave 2
