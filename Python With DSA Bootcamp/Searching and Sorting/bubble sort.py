def bubble_sort(my_list):
    size = len(my_list) - 1
    while (size != 0):
        for i in range(size):
            if(my_list[i] >= my_list[i+1]):
                temp = my_list[i]
                my_list[i] = my_list[i+1]
                my_list[i+1] = temp
        
        size -= 1
    return my_list
my_list = [10, 12, 54, 32, 1, 52, 13, 23]

print(bubble_sort(my_list))