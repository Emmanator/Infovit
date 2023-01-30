music_count = [156, 141, 35, 94, 88, 61, 111]


# Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List
class Linkedlist:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def search(self, data):
        current = self.head
        found = False
        while current and not found:
            if current.data == data:
                found = True
            else:
                current = current.next
        return found

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count


node1 = Node('A')
node2 = Node('B')
node3 = Node('C')

my_list = Linkedlist()
my_list.head = node1
node1.next = node2
node2.next = node3

print(my_list.size())


# Stack with Python List
class Stack1:
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


# Stack implementation with LinkedList
class Node2:
    def __init__(self, data, link):
        self.data = data
        self.next = link


class Stack2:
    def __init__(self):
        self.top = None
        self.size = 0

    def pop(self):
        node = self.top
        self.top = self.top.next
        self.size -= 1
        return node.data

    def push(self, data):
        self.top = Node2(data, self.top)
        self.size += 1

    def size(self):
        return self.size


my_stack = Stack2()
my_stack.push('1')
my_stack.push('2')
my_stack.push('3')

print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())


# Queue Implementation with Python List
class Queue1:
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


# Queue Implenentation with Doubly-linked List
class Node3:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Queue2:
    def __init__(self):
        self.head = None
        self.last = None

    def enqueue(self, data):
        if self.last is None:
            self.head = Node3(data)
            self.last = self.head
        else:
            self.last.next = Node3(data)
            self.last.next.prev = self.last
            self.last = self.last.next

    def dequeue(self):
        if self.head is None:
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return temp

    def size(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next


# Implementation of Selection Sort
def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


# Implementation of Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Implementation of Bubble Sort
def bubble_sort(arr):
    for pass_num in range(len(arr) - 1, 0, -1):
        for i in range(pass_num):
            if arr[i] > arr[i + 1]:
                print(i)
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp


bsort = music_count
bubble_sort(bsort)
print(bsort)


# Implementation of Quick Sort
def quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[1]
    # print(f'pivot is {pivot}')
    left = [i for i in arr[1:] if i <= pivot]
    # print(f'left is: {left}')
    right = [i for i in arr[1:] if i > pivot]
    # print(f'right is {right}')

    return quick_sort(left) + [pivot] + \
        quick_sort(right)


qsort = music_count
quick_sort(qsort)
print(qsort)


# Implementation of Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

msort = music_count
merge_sort(msort)
print(msort)