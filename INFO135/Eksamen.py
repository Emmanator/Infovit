# Insertion Sort
from abc import ABC, abstractmethod
from multiprocessing import Process


def insert_sort(input_list: list):
    n = len(input_list)
    for i in range(1, n):
        key = input_list[i]
        j = i - 1
        while j >= 0 and key < input_list[j]:
            input_list[j + 1] = input_list[j]
            j -= 1
        input_list[j + 1] = key


# Binary Search
def binary_search_func(imput_list: list, item):
    begin = 0
    end = len(imput_list) - 1
    found = False
    while begin <= end and not found:
        mid = (begin + end) // 2
        if imput_list[mid] > item:
            end = mid - 1
        elif imput_list[mid] < item:
            begin = mid + 1
        else:
            found = True
    return found


def my_func(input_list, item):
    insert_sort(input_list)
    return binary_search_func(input_list, item)


# Selection sort O(n^2)
def secret_sort(arr):
    n = len(arr)
    for i in range(n):
        min_ind = find_min_index(arr, i)
        temp = arr[min_ind]
        arr[min_ind] = arr[i]
        arr[i] = temp


def find_min_index(arr, start):
    n = len(arr)
    min_ind = start
    for i in range(start + 1, n):
        if arr[i] < arr[min_ind]:
            min_ind = i
    return min_ind


# Stack data structure
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def my_func(input_list):
    my_stack = Stack()
    my_list = []
    for item in input_list:
        my_stack.push(item)
        print(item)
    while not my_stack.is_empty():
        my_list.append(my_stack.pop())
        print(my_list)


my_list = [20, 30, 40, 50]
my_func(my_list)


# Factorial function
def fact_func(n):
    if n < 2:
        return 1
    return n * fact_func(n - 1)


# Factorial function, but with memo
def fact_memo(n):
    memo = [0] * (n + 1)
    memo[1], memo[0] = 1, 1

    for i in range(2, n + 1):
        memo[i] = i * memo[i - 1]
    return memo[n]


print(fact_func(10))
print(fact_memo(10))


# Abstract method decorator
class AbstractClass(ABC):
    @abstractmethod
    def my_method(self):
        pass


# Relationship between class shape and class Square
class Shape(ABC):
    @abstractmethod
    def compute_area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def compute_area(self):
        print(self.side * self.side)


# Interfacing (Implementing)

# Node class of a singly LinkedList
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


# Graph class remove node method
class Graph:
    graph = dict()
    searched = []

    def add_edge(self, node, neighbour):
        if node not in self.graph:
            self.graph[node] = [neighbour]
        else:
            self.graph[node].append(neighbour)

    def print_graph(self):
        print(self.graph)

    def print_edges(self):
        for nodes in self.graph:
            for neighbour in self.graph[nodes]:
                print(nodes, neighbour)

    # Example of Remove edges
    def remove_edges(self, node):
        if node in self.graph:
            del self.graph[node]
        for i in self.graph:
            if node in self.graph[i]:
                self.graph[i].remove(node)

    # Another example
    def remove_edges2(self, node):
        del self.graph[node]
        for nodes in self.graph:
            p = len(self.graph[nodes])
            if self.graph[nodes][p - 1] == node:
                del self.graph[nodes][p - 1]


# Process start
def my_function():
    pass


my_process = Process(target=my_function())
if __name__ == "__main__":
    my_process.start()
    my_process.join()

# Some shitty code
stack1 = Stack()
stack1.push(5)
stack1.push(4)
stack1.push(3)
stack1.push(2)
stack1.push(1)


def func1(input):
    output = Stack()
    while not input.is_empty():
        item = input.pop()
        output.push(item ** 2)
    return output


def func2(input):
    total = 1
    while not input.is_empty():
        total **= input.pop()
    return total


print(func2(func1(stack1)))
