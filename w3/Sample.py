import random

class Sample:
    def __init__(self, maximum):
        self.max = maximum
        self.n = 0
        self.sorted = False
        self.some = []

    def sampleInc(self, x):
        self.n = self.n + 1
        now = len(self.some)
        if now < self.max:
            self.sorted = False
            self.some[len(self.some)]=x
        elif random.uniform(0,1) < now / (self.n) :
            self.sorted = False
            self.some[int(random.uniform(0,1)*now)]=x
        return x

    def sampleSorted(self):
        if self.sorted == False:
            self.sorted = True
            self.some.sort()

        return self.some

    def nth(self, n):
        s = self.sampleSorted()
        return s[min(len(s), max(1, n)] #check this
                

if __name__ == "__main__":
    s = Sample(10)
