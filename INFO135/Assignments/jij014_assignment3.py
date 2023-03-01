# Assignment 1
# it takes the list, sets total to zero and length to length of the input string
# starting with "a1b2c3", it sets total to 0 + 97 (unicode number of a) + 6 (length of the input string)
# next it goes to second position in the string which is the int "1", and sets total to (103 + 49 + 6)
# it continues doing so for each string in the list and for each string returns
# (total unicode value + 6(for each character) % 19
# It then prints the value returned being 5 9 16 6

# Assignment 2
import hashlib as hl
import random


class HashClass:

    def __init__(self, id_num):
        self.id_num = self.hash_it(id_num)

    def hash_it(self, id_num):
        salt = random.randrange(1, 1000)
        test = str(id_num + salt)
        hash_str = hl.sha1(test.encode()).hexdigest()
        return hash_str

    def print_it(self):
        print(self.id_num)


employee1 = HashClass(11011999)
employee1.print_it()


# Assignment 3
def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i][1] < smallest[1]:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


def sort_and_print(liste):
    if len(liste) != 0:
        a = selection_sort(liste)
        print(f'The movie with the largest budget is: {a[-1][0]}')


list_of_tuples = [('Birds of Prey', 97.1),
                  ('Dolittle', 175.0),
                  ('The Gentlemen', 7.0),
                  ('Falling', 22.0)]

# print(selection_sort(list_of_tuples))
sort_and_print(list_of_tuples)

# Assignment 4
my_list = [10, 2, 5, 2, 0, 5, 6, 8, 5, 10, 2]
test = [1, 1, 2, 2, 2, 3, 3, 3, 4, 5]


def most_frequent_integer(liste):
    count = {}
    for i in liste:
        # print(f'{i} count: {(count.get(i, 0) + 1)}')
        count[i] = count.get(i, 0) + 1
    return max(count, key=count.get)


result4 = most_frequent_integer(test)
print(result4)

# Assignment 5
def magic_function(string, prefix=''):
    if len(string) <= 1:
        return string


    for i in string:
        print(i)
        # print(v)
    return
magic_function("abcd")
result5 = magic_function("abcd")
print(result5)