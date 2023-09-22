def insertion_sort(arr: list) -> list:
    """
    Take as input an array and return the sorted array using
    insertion sort.

    :param arr: The array to sort
    :return: The input array sorted using insertion sort
    """

    if len(arr) > 1:
        for i in range(1, len(arr)):
            while arr[i] < arr[i - 1] and i >= 1:
                temp = arr[i - 1]
                arr[i - 1] = arr[i]
                arr[i] = temp

                i -= 1

    return arr


arr_test = [10, 9, 6, 7]
print(insertion_sort(arr_test))
