import math
from sample import Sample

class Sym:

    def __init__(self, syms, f = lambda x:x):
        self.counts = {}
        self.mode = None
        self.most = 0
        self.n = 0
        self._ent = None
        self.syms = syms
        for s in self.syms:
            self.symInc(f(s))

        
    def symInc(self, x):
        if x == "?":
            return x
        self._ent = None
        self.n += 1
        old = self.counts.get(x,0)
        new = old and (old+1) or 1   
        self.counts[x] = new
        if new > self.most:
            self.most = new
            self.mode = x
        return x
        
    def symDec(self, x):
        self._ent = None
        if self.n > 0:
            self.n -= 1
            self.counts[x] -= 1
        return x
        
    def symEnt(self):
        if not self._ent:
            self._ent = 0
            p = 0
            for _, num in self.counts.items():
                p = num/self.n
                self._ent -= p*math.log(p, 2)
        
        return self._ent
        
