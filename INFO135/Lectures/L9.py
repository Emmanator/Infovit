# recursive fib
def fib(n):
    if n < 1:
        return n
    return fib(n - 1) + fib(n - 2)

# Much faster way to do fib,
def fib2(n):
    memo = [0] * (n + 1)
    memo[0], memo[1] = 0, 1
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]


# print(fib(40))
# print(fib2(40))

# Recursive method to determine the highest value bag to make
def knapsack_rec(capacity, weights, values, n):
    if n == 0 or capacity == 0:
        return 0

    elif weights[n - 1] > capacity:
        return knapsack_rec(capacity, weights, values, n - 1)

    else:
        tmp1 = knapsack_rec(capacity, weights, values, n - 1)

        tmp2 = values[n - 1] + knapsack_rec(capacity - weights[n - 1], weights, values, n - 1)

        return max(tmp1, tmp2)


def knapsack_dp(capacity, weights, values, n):
    grid = [[0 for x in range(capacity + 1)]
            for x in range(n + 1)]

    for item in range(n + 1):
        for cap in range(capacity + 1):

            if item == 0 or cap == 0:
                grid[item][cap] = 0

            elif weights[item - 1] <= cap:
                grid[item][cap] = max(values[item - 1] +
                                      grid[item - 1][cap - weights[item - 1]],
                                      grid[item - 1][cap])

            else:
                grid[item][cap] = grid[item - 1][cap]

    return grid[n][capacity]


item_val = [50, 100, 150, 200]

item_wt = [8, 16, 32, 40]
total_cap = 64
n_items = len(item_val)

print(knapsack_rec(total_cap, item_wt, item_val, n_items), '$')
print(knapsack_dp(total_cap, item_wt, item_val, n_items), '$')
