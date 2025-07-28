def linear_search(arr, target):
    size = len(arr)
    for i in range(size):
        if arr[i] == target:
            return i
    return -1

my_list = [1, 12, 34, 23, 35, 87, 38]
target = 23
print(linear_search(my_list, target))