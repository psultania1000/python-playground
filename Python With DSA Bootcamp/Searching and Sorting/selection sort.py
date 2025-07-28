def selection_sort(lst):
    size = len(lst)
    for i in range(size):
        min = lst[i]
        index = i
        for j in range(i+1, size):
            if(min > lst[j]):
                min = lst[j]
                index = j
        lst[i], lst[index] = lst[index], lst[i]
    return lst

my_list = [56, 43, 34, 32, 31, 21, 12]
print(selection_sort(my_list))