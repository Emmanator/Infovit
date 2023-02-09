import math


# Assignment 1
def binary_search_big_o(l):
    return math.ceil(math.log(l) / math.log(2))


# a) 18
print(binary_search_big_o(171476))
# b) 21
print(binary_search_big_o(1100373))
# c) 18
print(binary_search_big_o(260000))


# Assignment 2
class LinkedList:
    def __init__(self):
        self.head = None


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def create_linked_list():
    a = LinkedList()
    b = LinkedList()
    c = LinkedList()
    a.head = 1
    b.head = 2
    c.head = 3
    a.tail = b
    b.tail = c
    c.tail = LinkedList()
    return a


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.next = b
b.next = c
c.next = d

def print_list(u):
    while u is not None:
        print(u.data)
        u = u.next

print_list(a)

# Assignment 3
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()



def reverse_list(l):
    stack = Stack()
    for i in l:
        stack.push(i)
    reverse = []
    while not stack.is_empty():
        reverse.append(stack.pop())
    return reverse


print(reverse_list([1, 2, 3, 4, 5]))
