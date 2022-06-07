def faktorial(n):
    print(f'oooooooo nuymbers: {n}')
    if n <= 1:
        return 1
    else:
        return faktorial(n - 1) * n


a = faktorial(20)
b = faktorial(16)

print(a / b)