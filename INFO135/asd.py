memo = dict()

def fact_func2(n):
    if n < 2:
        return 1

    if n not in memo:
        print(f"Computing factorial of {n}")
        memo[n] = n * fact_func2(n - 1)

    return memo[n]


for i in range(1):
    print(fact_func2(i))