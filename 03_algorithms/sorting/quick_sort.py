def quicksort(array, start, end):
    # base case: size <= 1
    if start >= end:
        return

    # partition the array and get pivot index
    pivot_index = partition(array, start, end)

    # recursive calls on sublists
    quicksort(array, start, pivot_index - 1)
    quicksort(array, pivot_index + 1, end)


def partition(array, start, end):
    pivot_value = array[end]
    pivot_index = start

    for index in range(start, end + 1):
        if array[index] <= pivot_value:
            # Swap array[index] and array[pivot_index]
            array[index], array[pivot_index] = array[pivot_index], array[index]
            pivot_index += 1

    return pivot_index - 1


# Example usage:
arr = [8, 4, 7, 3, 10, 2]
quicksort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)