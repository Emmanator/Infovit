# Assignmen 1
def selection_sort_one_pass(array):
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
        if passes == 3:
            print(f'{array}')
    return

test = [90, 78, 56, 1239, 1, 1289, 123, 6363, 7127]
selection_sort_one_pass(test)