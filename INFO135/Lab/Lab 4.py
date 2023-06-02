import math

# Exercise 1

n = 8949
# a)
print(n)


# b)
# c)

# Exercise 2
def one_pass(liste, index):
    sub_liste = liste[index:]
    smallest = min(sub_liste)
    smallest_index = sub_liste.index(smallest) + index
    liste[index], liste[smallest_index] = liste[smallest_index], liste[index]
    return liste


def more_pass(liste):
    for i in range(len(liste) - 1):
        one_pass(liste, i)
    return liste


liste = [-4, 0, 1, 9, 0]

# liste = [1]
print(more_pass(liste))

# Exercise 3
nuts = ['@', '#', '$', '%', '^', '&']
bolts = ['$', '%', '&', '^', '@', '#']

# this is a brute force method without a sorting algorithm
def nuts_and_bolts(a, b):
    nuts = []
    bolts = []
    for i in a:
        for j in b:
            if i == j:
                nuts.append(i)
                bolts.append(j)

    print(nuts)
    print(bolts)
    return


nuts_and_bolts(nuts, bolts)


def partition(arr, low: int, high: int):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1

            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])

    return i + 1


def quick_sort(arr: list, low: int, high: int):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


quick_sort(nuts, 0, (len(nuts) - 1))
quick_sort(bolts, 0, (len(bolts) - 1))

print(nuts)
print(bolts)