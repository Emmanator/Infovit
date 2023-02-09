# Example Recursion code
# def look_for_key(box):
#     for item in box:
#         if item.is_a_box():
#             look_for_key(item):
#         elif:
#             print('found key')


# Add all numbers up to N together
def sum(n):
    if n == 0:
        return 0
    else:
        # print(n)
        return n + sum(n - 1)


print(sum(5))


# fib
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# print(fib(100))

# Backtracking Queen puzzle thing
COLUMNS = 'abcde'
num_queens = len(COLUMNS)
accept = 1
CONTINUE = 2
ABANDON = 3
count = 0


def extend(partial_sol):
    results = []
    row = len(partial_sol) + 1

    for column in COLUMNS:
        new_solution = list(partial_sol)
        new_solution.append(column + str(row))
        results.append(new_solution)

    return results


def attacks(p1, p2):
    column1 = COLUMNS.index(p1[0]) + 1
    row1 = int(p1[1])

    column2 = COLUMNS.index(p2[0])
    row2 = int(p2[1])

    return (row1 == row2 or
            column1 == column2 or
            abs(row1 - row2) == abs(column1 - column2))


def examine(partial_sol):
    for i in range(len(partial_sol)):
        for j in range(i + 1, len(partial_sol)):
            if attacks(partial_sol[i], partial_sol[j]):
                return ABANDON

    if len(partial_sol) == num_queens:
        return accept
    else:
        return CONTINUE


def solve(partial_sol):
    global count
    exam = examine(partial_sol)
    if exam == accept:
        count += 1
        print(partial_sol)

    elif exam != ABANDON:
        for p in extend(partial_sol):
            solve(p)


# solve([])
# print(count)

def sequential_search(a_list, item):
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found
