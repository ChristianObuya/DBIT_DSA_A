def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        pos = arr[i]
        j = i - 1

        # Repeat while POS <= ARR[J]
        while j >= 0 and pos <= arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = pos
    return arr

arr = [9, 5, 2, 7, 1]
insertion_sort(arr)
print("Sorted array:", arr)