class Structure:

    def __init__(self):
        self.array = []
        self.size = 0

    def __getitem__(self, item):
        return self.array[item]

    def push_back(self, n):
        self.array.append(n)
        self.size += 1

    def pop_front(self):
        self.array.pop(0)
        self.size -= 1

    def front(self):
        return self.array[0]

    def back(self):
        return self.array[len(self.array)-1]

    def get_size(self):
        return self.size
