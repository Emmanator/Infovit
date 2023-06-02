# Exercise 1
def selection_sort(array):
    length = len(array)
    passes = 0
    print(f'#{passes}: {array}')

    for i in range(length - 1):
        min_idx = i
        passes += 1

        for j in range(i + 1, length):
            if array[j] < array[min_idx]:
                min_idx = j

        array[i], array[min_idx] = array[min_idx], array[i]
        print(f'#{passes}: {array}')
    return


test = [90, 78, 56, 1239, 1, 1289, 123, 6363, 7127]
selection_sort(test)
# Exercise 2
from large_list import liste
from operator import itemgetter


def llist_sort(arr):
    b = []
    for i in arr:
        if (i[0] + i[1]) == i[2]:
            b.append(i)
    return b


a = llist_sort(liste)


def sort(arr):
    data = arr
    return sorted(data, key=itemgetter(2))


def quick_sort(arr):
    for pass_num in range(len(arr) - 1, 0, -1):
        for i in range(pass_num):
            if arr[i][-1] > arr[i + 1][-1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
    return arr


print(llist_sort(sort(a)))
print(llist_sort(quick_sort(a)))


# Exercise 3
def find_anagram(s1: str, s2: str):
    c1 = list(s1.lower().replace(' ', ''))
    c2 = list(s2.lower().replace(' ', ''))
    if quick_sort(c1) == quick_sort(c2):
        # print(c1, c2)
        return 'is anagram! :D'
    else:
        # print(c1, c2)
        return 'cry'


print(find_anagram('The Detectives', 'Detect Thieves'))
