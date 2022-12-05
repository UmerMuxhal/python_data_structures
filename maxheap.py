class MaxHeap:

    def __init__(self, items=[]):
        super().__init__()
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.__float_up(len(self.heap) - 1)

    def __parent(self, index):
        return index // 2

    def __left(self, index):
        return index * 2

    def __right(self, index):
        return (index * 2) + 1

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __float_up(self, index):
        parent = self.__parent(index)
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__float_up(parent)

    def __bubble_down(self, index):
        left = self.__left(index)
        right = self.__right(index)
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubble_down(largest)

    def insert(self, item):
        self.heap.append(item)
        self.__float_up(len(self.heap) - 1)

    def get_max(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def remove_max(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            removed = self.heap.pop()
            self.__bubble_down(1)
        elif len(self.heap) == 2:
            removed = self.heap.pop()
        else:
            removed = False
        return removed

    def clear(self):
        for i in range(len(self.heap) - 1, 0, -1):
            print(i)
            del (self.heap[i])

    def __str__(self):
        # print(self.heap)
        # return str(', '.join(self.heap))
        return str(self.heap[1:])

    def print(self):
        size = len(self.heap)
        for i in range(1, (size // 2) + 1):
            left = lambda x: self.heap[self.__left(i)] if self.__left(i) < size else None
            right = lambda x: self.heap[self.__right(i)] if self.__right(i) < size else None
            # if self.__left(i) < size and self.__right(i) < size:
            #     print(" PARENT : " + str(self.heap[i]) +
            #           " LEFT CHILD : " + str(self.heap[2 * i]) +
            #           " RIGHT CHILD : " + str(self.heap[2 * i + 1]))
            print(" PARENT : " + str(self.heap[i]) +
                  " LEFT CHILD : " + str(left(i)) +
                  " RIGHT CHILD : " + str(right(i)))


max_heap = MaxHeap()
for i in "aeiou": max_heap.insert(i.upper())
print(max_heap)
max_heap.print()
max_heap.clear()
print(max_heap)
for i in "123456789":
    max_heap.insert(i)
    print(max_heap)
    max_heap.print()
    print("------------------------------------")
print(max_heap)
