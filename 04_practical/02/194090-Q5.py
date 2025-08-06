numbers = [12, 3, 45, 65, 88]

def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

print(linear_search(numbers, 45))
print(linear_search(numbers, 0))