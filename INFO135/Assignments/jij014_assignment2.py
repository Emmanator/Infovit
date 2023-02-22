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
selection_sort(ass1)


# Assignment 2
def bubble_sort_three_passes(arr):
    for pass_num in range(len(arr) - 1, 0, -1):
        for i in range(0, 3):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
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
    print(arr)
    new_list = []
    for i in arr:
        if len(new_list) == 0 or (arr[i] != new_list[-1]):
            new_list.append(i)
    return new_list


my_list = [5, 4, 3, 2, 1, 2, 3, 4, 5, 2]
new_list = sort_and_rem_dup(my_list)
print(new_list)


# Assignment 4
def check_palindrome(word):
    for i in range(0, (len(word) // 2)):  # this code checks half the amount of letters the code beneathe checks
        if word[i] != word[-1 - i]:  # marginally faster
            return 'is not palindrome'
    return 'is Palindrome'

    # if word == word[::-1]:
    # return 'is palindrome'
    # else:
    # return 'is not palindrom'


print(check_palindrome('saippuakivikauppias'))
