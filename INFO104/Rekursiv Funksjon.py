def faktorial(n):
    print(f'oooooooo nuymbers: {n}')
    if n <= 1:
        return 1
    else:
        return faktorial(n - 1) * n


print(faktorial(52))