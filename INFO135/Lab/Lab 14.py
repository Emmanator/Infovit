def fun(n):
    if n < 4:
        return 1
    elif n == 4:
        return 4
    else:
        return fun(n - 1) + fun(n - 2) + fun(n - 3) + fun(n - 4)

def fun2(n):
    memo = [0] * (n+1)
    memo[0], memo[1], memo[2], memo[3] = 1, 1, 1, 1
    memo[4] = 4

    for i in range(5, n+1):
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3] + memo[i-4]
    return memo

print(fun2(5))
