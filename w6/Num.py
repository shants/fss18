from Sample import Sample
import math

class Num:
    def __init__(self,m=0):
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.sd = 0
        self.lo = math.pow(10,32)
        self.hi = -1 * math.pow(10,32)
        self._some = Sample(m)
        self.w = 1

    def nums(self,t, f=None):
        if  f == None:
            f= lambda x: x
            
        n = Num(len(t))
        for x in t:
            n.numInc(f(x))
        return n

    def numInc(self, x):
        if x == '?':
            return x

        self.n = self.n + 1
        self._some.sampleInc(x)
        d = x - self.mu
        self.mu = self.mu + d/self.n
        self.m2 = self.m2 + d * (x-self.mu)
        if x > self.hi:
            self.hi = x
        if x < self.lo:
            self.lo = x

        if ( self.n >= 2):
            self.sd = (self.m2 / (self.n - 1 + math.pow(10, -32))) ** 0.5

        return x

    def numDec(self, x): 
        if (x == "?"):
            return x

        if (self.n == 1):
            return x

        self.n  = self.n - 1
        d = x - self.mu
        self.mu = self.mu - d/self.n
        self.m2 = self.m2 - d*(x- self.mu)
        if (self.n>=2):
            self.sd = (self.m2 / (self.n - 1 + math.pow(10, -32))) ** 0.5
            
        return x


    def numNorm(self,x):
        # what is this ???
        return x=="?" and 0.5 or (x-self.lo) / (self.hi-self.lo + math.pow(10,-32))

    def numXpect(self,j):
        n = self.n + j.n + 0.0001
        return self.n/n * self.sd+ j.n/n * j.sd

