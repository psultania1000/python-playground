import sys

l1 = [] # stores as call by reference

# print("initial size: ",sys.getsizeof(l1))

# for i in range(0, 17):
#     l1.append(i)
#     l1.append("i")
#     print(f"{i} --> {sys.getsizeof(l1)}")
    
# a = 1000000000000
# b = 1000000000000

a = int("10000")
b = int("10000")

print(id(a), " ", id(b))

