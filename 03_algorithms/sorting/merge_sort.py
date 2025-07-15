def merge_sort(array, start, end):
    if start >= end:
        return

    half = (start + end) // 2
    merge_sort(array, start, half)         # Split and sort left half
    merge_sort(array, half + 1, end)       # Split and sort right half
    merge(array, start, half, end)         # Merge the two halves

def merge(array, start, half, end):
    temp_array = [0] * (end - start + 1)
    index1 = start
    index2 = half + 1
    new_index = 0

    while index1 <= half and index2 <= end:
        if array[index1] < array[index2]:
            temp_array[new_index] = array[index1]
            index1 += 1
        else:
            temp_array[new_index] = array[index2]
            index2 += 1
        new_index += 1

    while index1 <= half:
        temp_array[new_index] = array[index1]
        index1 += 1
        new_index += 1

    while index2 <= end:
        temp_array[new_index] = array[index2]
        index2 += 1
        new_index += 1

    for i in range(len(temp_array)):
        array[start + i] = temp_array[i]

arr = [8, 3, 7, 2, 5, 1]
merge_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)