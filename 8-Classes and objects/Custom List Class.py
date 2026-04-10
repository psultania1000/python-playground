import ctypes
class CustomList:
    def __init__(self):
        initialCapacity = 1
        self.capacity = initialCapacity
        self.size = 0
        self.array = self.__create_array(self.capacity)
        
    def __create_array(self, capacity):
        # creating a new referential array with given capacity
        return (capacity * ctypes.py_object)()
    
    def __resize(self, new_capacity):
        new_array = self.__create_array(new_capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]
            
        self.array = new_array
        self.capacity = new_capacity

    def append(self, item):
        if self.size == self.capacity:
            self.__resize(2*self.capacity)
        
        self.array[self.size] = item
        self.size += 1
    
    def __len__(self):
        return (self.size)
    
    def __str__(self):
        output = ''
        for i in range(self.size - 1):
            output = output + str(self.array[i]) + ', '
        output = output + str(self.array[self.size - 1])
        
        return '['+output+']'

    def pop(self):
        if self.size == 0:
            return "Empty List, IndexError: pop from empty list"
        last_value = self.array[self.size - 1]
        self.size -= 1
        return last_value
    
    def __getitem__(self, index):
        if (index >= 0 and index < self.size):
            return self.array[index]
        else:
            return "Index Error"
        
    def clear(self):
        self.size = 0
        
    def insert(self, index, item):
        if self.size == self.capacity:
            self.__resize(2 * self.capacity)
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i-1]
        self.array[index] = item
        self.size += 1
        
        
myList = CustomList()
myList.append(1)
myList.append(2)
# myList.append(3)
# myList.append(4)

myList.insert(1, 100)

print(myList)