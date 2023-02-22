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
    passes = 0
    for pass_num in range(len(arr) - 1, 0, -1):
        for i in range(3):
            if arr[i] > arr[i + 1]:
                # print(arr)
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
    return arr


ass2 = [210, 15, 111, 90, 45, 120, 150, 200, 100, 140]
print(bubble_sort_three_passes(ass2))

# print(range(3))
