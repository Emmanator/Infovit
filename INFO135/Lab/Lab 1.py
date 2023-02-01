# Lab 1
import math


# Classes
# Exercise 1
class Person:

    def __init__(self, name: str):
        self.person = name

    def greets(self, name):
        print(f'{self.person}: "Hello, {name.person}!"')


alice = Person('Alice')
bob = Person('Bob')
charlie = Person('Charlie')
alice.greets(bob)
alice.greets(charlie)


# Exercise 2
class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = 10000

    def get_fullname(self):
        return f'{self.firstname} {self.lastname}'

    def print_email(self):
        return f'{self.firstname}.{self.lastname}@company.no'

    def increase_salary(self, rate: int):
        return self.salary * rate


# Binary Search
# Exercise 1
# a) Can perform Binary Search on 1, 3, 4, 5
# b) O(log n)


# Exercise 2

def binary_search_big_o(l):
    return math.ceil(math.log(l) / math.log(2))


def bad_big_o(l):
    return (l)


print(binary_search_big_o(10000))
print(bad_big_o(10000))
# Extra task 2
text = 'haha ball funny in yesyes'


def reverse_text(t: str):
    x = t.split(' ')
    x.reverse()
    return ' '.join(x)


print(reverse_text(text))
