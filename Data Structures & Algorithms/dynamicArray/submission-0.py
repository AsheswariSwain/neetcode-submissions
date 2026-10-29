class DynamicArray:
    
    def __init__(self, capacity: int):
        assert capacity > 0, "Capacity must be greater than 0"
        self.capacity = capacity
        self.size = 0
        self.arr = [None]*capacity



    def get(self, i: int) -> int:
        assert  0 <= i <self.size, " Out of bound"
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        assert 0 <= i < self.size , "Out of bound"
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        if self.size == self.capacity :
            self.resize()
        
        self.arr[self.size] = n
        self.size += 1


    def popback(self) -> int:
        assert self.size > 0, "No element available in Array"
        val = self.arr[self.size-1]
        self.size -=1
        return val
 

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_arr = [None]* new_capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = new_capacity



    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
