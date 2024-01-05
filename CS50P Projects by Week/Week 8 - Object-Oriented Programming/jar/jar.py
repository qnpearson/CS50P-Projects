#Cannopt alter class method parameters, but can add your own methods
#import emoji

class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size*'🍪'

    def deposit(self, n):
        self.size += int(n)

    def withdraw(self, n):
        self.size -= int(n)

    @property #Getter
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not capacity:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, size) -> int:
        if 0 <= size <= self.capacity:
            self._size = size
        else:
            raise ValueError("Invalid Size")
