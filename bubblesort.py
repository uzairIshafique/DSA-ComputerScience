def bubble_sort(arr: list) -> list:
    """
    Takes an array as input and returns a sorted array using bubble sort.

    :param arr: The array to be sorted
    :return: The sorted array to be returned
    """

    end = len(arr)

    for i in range(end):
        for j in range(end - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp

    return arr


arr_test = [10, 9, 8, 7]

print(bubble_sort(arr_test))
