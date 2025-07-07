class Counter:
    def __init__(self):
        self.count = 0

    def reset(self, initValue=0):
        self.count = initValue

    def increment(self):
        self.count +=1

    def get(self):
        return self.count

a = Counter()
b = Counter()

a.reset()
a.increment()
print(a.get())
