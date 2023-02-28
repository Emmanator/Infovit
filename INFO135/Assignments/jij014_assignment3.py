# Assignment 1
# it takes the list, sets total to zero and length to length of the input string
# starting with "a1b2c3", it sets total to 0 + 97 (unicode number of a) + 6 (length of the input string)
# next it goes to second position in the string which is the int "1", and sets total to total (103 + 49 + 6)

my_list = ['a1b2c3', 'CiTiBnk', '232323', 'myLaptop']


def hash_function(input_string, table_size):
    total = 0
    length = len(input_string)
    for pos in range(length):
        print(ord(input_string[pos]))
        print(total + ord(input_string[pos]) + length)
        total = total + ord(input_string[pos]) + length

    print(total)
    return total % table_size


for item in my_list:
    print(hash_function(item, 19), 'aaa')
