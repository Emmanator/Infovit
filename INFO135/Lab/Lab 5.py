# Exercise 1
class MiniBank:
    def __init__(self, name):
        self.name = name

    def bills(self, bills):
        self.bills = bills

    def sort_bills(self):
        self.bills = sorted(self.bills)


jeff = MiniBank('jeff')
jeff.bills([('water', 2200), ('wolfram alpha', 150), ('electric', 5000)])


# print(jeff.sort_bills())

# Exercise 2

def fib(n):
    if n < 1:
        return n
    return fib(n - 1) + fib(n - 2)


# print(fib(9))

# Exercise 3

n = 15

for i in range(n):
    # print(f': {i} ')
    for j in range(n):
        # print(f'{j} ', end='')
        if i == j or ((n - j - 1) == i):
            # print(f'if: {i:02d} {j:02d}, ({n:02d} - {j:02d} - 1 =) {(n - j - 1):02d}')
            print('*', end='')
        else:
            print(' ', end='')
    print('')


def a_space_classic(n):
    z = n - 1
    x = 1
    for i in range(0, n):
        for i in range(0, z):
            print(' ', end='')
        for i in range(0, x):
            print('+', end='')
        for i in range(0, z):
            print(' ', end='')
        x = x + 2
        z = z - 1
        print()

a_space_classic(3)
