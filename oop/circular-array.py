class CircularArray:
    def __init__(self, size):
        self.items = [None]*size
        self.head = 0

    def convert(self, index):
        if index < 0:
            index += len(self.items)
        return (self.head+index) % len(self.items)

    def rotate(self, shiftRightBy):
        self.head = self.convert(shiftRightBy-1)

    def get(self, index):
        if index < 0 or index >= len(self.items):
            raise Exception("Out of bound")

        return self.items[self.convert(index)]

    def set(self, index, item):
        self.items[self.convert(index)] = item


array = CircularArray(5)

array.set(0, "a")
array.set(1, "b")
array.set(2, "c")
array.set(3, "d")
array.set(4, "e")

array.rotate(3)

print(array.get(0))
print(array.get(1))
print(array.get(2))
print(array.get(3))
print(array.get(4))
