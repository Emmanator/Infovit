# Exercise 1
def factorial(n):
    if n == 1 or 0:
        return 1
    return n * factorial(n - 1)

fac = factorial(5)
print(fac)