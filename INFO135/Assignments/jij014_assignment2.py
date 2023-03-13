# Assignment 1
def selection_sort(array):
    length = len(array)
    passes = 0
    # print(f'#{passes}: {array}')

    for i in range(length - 1):
        min_idx = i
        passes += 1

        for j in range(i + 1, length):
            if array[j] < array[min_idx]:
                min_idx = j

        array[i], array[min_idx] = array[min_idx], array[i]
        # print(f'#{passes}: {array}')
        if passes == 3:
            print(f'after 3 passes: {array}')
    return


ass1 = [1001, 1030, 1050, 1020, 300, 1080, 1100]


# selection_sort(ass1)


# Assignment 2
def bubble_sort_three_passes(arr):
    for pass_num in range(0, 3):
        # print(arr)
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] < arr[i - 1]:
                temp = arr[i]
                arr[i] = arr[i - 1]
                arr[i - 1] = temp
    return arr


ass2 = [210, 15, 111, 90, 45, 120, 150, 200, 100, 140]

print(bubble_sort_three_passes(ass2))


# Assignment 3
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def sort_and_rem_dup(arrr):
    arr = insertion_sort(arrr)
    # print(arr)
    new_list = []
    for i in arr:
        # print(i)
        if len(new_list) == 0 or (i != new_list[-1]):
            new_list.append(i)
    return new_list


my_list = [5, 4, 3, 2, 1, 2, 3, 4, 5, 2]
new_list = sort_and_rem_dup(my_list)
print(new_list)


# Assignment 4
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)]

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def check_palindrome(word):
    s = Stack()
    q = Queue()

    for i in word:
        s.push(i)
        q.enqueue(i)

    while not q.is_empty():
        if s.pop() != q.dequeue():
            return 'not palindrome'
    return 'is palindrome'

# print(check_palindrome('oiguawdoiuygladw'))
