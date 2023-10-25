numbers = [0, 1, 2, 4]

for i in range(10):
    a = numbers[-1] + numbers[-2] + 1
    numbers.append(a)
    print(numbers)