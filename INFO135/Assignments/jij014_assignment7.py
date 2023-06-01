# Exercise 1:
# n^3

# Exercise 2:
# n^4 + n^3 + 9n^2 + n log n + 5 <= c * n^4
# n^4 <= 1n^4
# n^3 <= 1n^4
# 9n^2 <= 9n^4
# n log n <= n^4
# 5 <= 5n^4
# n^4 + n^3 + 9n^2 + n log n + 5 <= (1+1+9+1+5) * n^4
# c = 17

# Exercise 3:
# a) n * log(n)
def my_func1(inputs):
    n = len(inputs)
    result = 0
    for i in range(n):
        j = 1
        while j < n:
            result += inputs[i] * inputs[j]
            j *= 2
    return result


# b) n^2
def my_func2(inputs):
    n = len(inputs)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if inputs[j] > inputs[j + 1]:
                tmp = inputs(j)
                inputs[j] = inputs[j + 1]
                inputs[j + 1] = tmp


# Exercise 4:
my_list = [1, 2, 3, 4, 5]


def solve_problem(list):
    n = len(list)
    k = []
    for i in range(n):
        a = 0
        for j in list[:i + 1]:
            a += j
        k.append(a / (i + 1))
    return k


# Calculates average of first i numbers n times
# bigO= n^2

def solve_problem_butt_faster(list):
    n = len(list)
    sums = []
    for i in range(n):
        if i == 0:
            sums.append(list[i])
        else:
            sums.append(sums[i - 1] + list[i])

    avgs = []
    for j in range(n):
        avgs.append((sums[j] / (j + 1)))
    return avgs
# It contains two for loops
# The first loop calculates the running sums by adding the (i - 1)-st element
# in sums with the i-th element in list.
# The second loop converts the sums into averages by dividing it over number of elements summed
# and puts it into avgs
# bigO = O(n)
print(solve_problem(my_list))
print(solve_problem_butt_faster(my_list))
