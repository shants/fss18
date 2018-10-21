import math
from sample import Sample

class Num:

    def __init__(self, nums, f = lambda x:x):        
        self.n=0
        self.mu=0
        self.m2=0
        self.sd=0 
        self.lo=10**32 
        self.hi=-10**32 
        self.max_val = len(nums)
        self._some=Sample(self.max_val)
        self.w=1

        for n in nums:
            self.numInc(f(n))       
        
    def nums(self, t, f = None):
        if f == None:
            f = lambda x: x
        n = Num(len(t))
        for x in t:
            n.numInc(f(x))
        return n
        
    def numInc(self, x):
        if x == "?":
            return x
        x = float(x)
        self.mu = float(self.mu)
        self.n += 1
        self._some.sampleInc(x)
        d = x - self.mu
        self.mu += (d/self.n)
        self.m2 += (d*(x - self.mu))
        if x > self.hi:
            self.hi = x
        if x < self.lo:
            self.lo = x
        if self.n >= 2:
            self.sd = (self.m2/(self.n - 1 + math.pow(10, -32)))**0.5
        return x
    
    def numDec(self, x):
        if x == "?" or self.n == 1:
            return x
        self.n -= 1
        d = x - self.mu
        self.mu -= (d/self.n)
        self.m2 -= d*(x - self.mu)
        if self.n >= 2:
            self.sd = (self.m2/(self.n - 1 + math.pow(10, -32)))**0.5
        return x
    
    def numNorm(self, x):
        return 0.5 if x=="?" else (x - self.lo)/(self.hi - self.lo + math.pow(10,-32))
        
    def numXpect(self, i, j):
        n = i.n + j.n + 0.0001
        return (i.n/n * i.sd + j.n/n * j.sd)
    
