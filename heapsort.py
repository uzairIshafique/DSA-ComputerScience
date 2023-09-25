def max_heap(arr: list, i: int, n: int):
    """
    Take as input an array and return a list sorted using heap sort.

    :param n:   The length of the array
    :param i:   The index of the value to check
    :param arr: The array to be sorted
    """

    while True:
        left = i*2+1   # left child of the node
        right = i*2+2  # right child of the node

        if max(left, right) < n:
            if max(arr[left], arr[right]) < arr[i]:
                break
            elif arr[left] > arr[right]:
                arr[i], arr[left] = arr[left], arr[i]
                i = left
            else:
                arr[i], arr[right] = arr[right], arr[i]
                i = right
        elif left < n:
            if arr[left] > arr[i]:
                arr[i], arr[left] = arr[left], arr[i]
                i = left
            else:
                break
        elif right < n:
            if arr[right] > arr[i]:
                arr[i], arr[right] = arr[right], arr[i]
                i = right
            else:
                break
        else:
            break


def heap_sort(arr: list):
    """
    The helper method used to call the max_heap() method.

    :param arr: The array to be passed to max_heap()
    """
    for i in range((len(arr) - 2) // 2, -1, -1):
        max_heap(arr, i, len(arr))

    for j in range((len(arr) - 1), 0, -1):
        arr[j], arr[0] = arr[0], arr[j]
        max_heap(arr, 0, j)


arr_test = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
heap_sort(arr_test)
print(arr_test)
