def insertion_sort(lst):
    size = len(lst)
    
    for i in range(size - 1):
        ele = lst[i+1]
        index = i + 1
        print(ele, " ", index)
        for j in range(i+1):
            print(j, " ", lst[j], " ", ele)
            if (ele < lst[j]):
                index = j
                break;
        # if (index != i+1):     
        for k in range(i + 1, index, -1):
            print(k, " ", i, " ", index)
            lst[k] = lst[k-1]
            
        lst[index] = ele
        print("lst: ", lst)
    return lst

my_list = [10, 56, 43, 34, 12, 21, 32, 31, 9, 10]
print(insertion_sort(my_list))