def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while(low<=high):
        mid = (low + high) // 2
        
        if(arr[mid] == target):
            return mid
        elif (arr[mid] > target):
            high = mid - 1
        elif (arr[mid] < target):
            low = mid + 1  
    return -1


my_list = [1, 12, 23, 34, 35, 38, 87]
target = 87
print(binary_search(my_list, target))