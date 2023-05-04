# Exercise 1:
# n^3

# Exercise 2:
# n^4 + n^3 + 9n^2 + n log n + 5 <= c * n^4
# n^4 <= 1n^4
# n^3 <= 1n^4
# 9n^2 <= 9n^4
# n log n <= n^4
# 5 <= 5n^4
# n^4 + n^3 + 9n^2 + n log n + 5 <= (1+1+9+7+5) * n^4

# Exercise 3:
# a) Seems like of just BigO(n)
def my_func1(inputs):
    n = len(inputs)
    result = 0
    for i in range(n):
        j = 1
        while j < n:
            result += inputs[i] * inputs[j]
            j *= 2
    return result


# b)
def my_func2(inputs):
    n = len(inputs)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if inputs[j] > inputs[j + 1]:
                tmp = inputs(j)
                inputs[j] = inputs[j + 1]
                inputs[j + 1] = tmp

# Exercise 4:
