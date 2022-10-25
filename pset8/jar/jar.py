class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("jar size can't be greater than its capacity")
        else:
            self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Withdrawal can't exceed current size")
        else:
            self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity > 0:
            self._capacity = capacity
        else:
            raise ValueError("Capacity cannot be negative")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if not size:
            self._size = 0
        else:
            self._size = size
