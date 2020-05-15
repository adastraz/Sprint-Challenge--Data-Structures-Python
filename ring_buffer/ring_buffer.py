class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stuff = []

    def append(self, item):
        if len(self.stuff) < self.capacity:
            self.stuff.append(item)
        else:
            self.stuff.remove(self.stuff[0])
            self.stuff.append(item)

    def get(self):
        return(self.stuff)