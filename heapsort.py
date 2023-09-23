def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def sift_down(arr, i, upper):
    while True:
        l, r = i * 2 + 1, i * 2 + 2

        if max(l, r) < upper:
            if arr[i] >= max(arr[l], arr[r]):
                break
            elif arr[l] > arr[r]:
                swap(arr, i, l)
                i = l
            else:
                swap(arr, i, r)
                i = r
        elif l < upper:
            if arr[l] > arr[i]:
                swap(arr, i, l)
                i = l
            else:
                break
        elif r < upper:
            if arr[r] > arr[i]:
                swap(arr, i, r)
                i = r
            else:
                break
        else:
            break


def heapsort(arr):
    for j in range(len(arr) - 2 // 2, -1, -1):
        sift_down(arr, j, len(arr))

    for end in range(len(arr) - 1, 0, -1):
        swap(arr, 0, end)
        sift_down(arr, 0, end)


arr_test = [5, 16, 8, 14, 20, 1, 26]
heapsort(arr_test)
print(arr_test)
