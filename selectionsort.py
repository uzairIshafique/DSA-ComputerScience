def selection_sort(arr: list) -> list:
    """
    Take as input an array and sort it using the selection
    sort and return the sorted array.

    :param arr: The array to be sorted using selection sort
    :return: The sorted array to be returned
    """

    n = len(arr)

    for i in range(n):
        minimum = i

        for j in range(i + 1, n):
            compare_element = arr[j]
            if compare_element < arr[minimum]:
                minimum = j

        temp = arr[i]
        arr[i] = arr[minimum]
        arr[minimum] = temp

    return arr


arr_test = [34, 21, 4, 5, 79]

print(selection_sort(arr_test))
