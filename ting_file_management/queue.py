class Queue:
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def enqueue(self, value):
        self.list.append(value)

    def dequeue(self):
        return self.list.pop(0)

    def search(self, index):
        if index > self.__len__() - 1 or index < 0:
            raise IndexError
        return self.list[index]
