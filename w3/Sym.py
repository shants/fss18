import math

class Sym:
    def __init__(self):
        self.counts={}
        self.mode = None
        self.most = 0
        self.n = 0
        self._ent = None


    def syms(self,t, f = None):
        if f == None:
            f =  lambda x: x
        s = Sym()
        for x in t:
            s.symInc(f(x))
        return s

    def symInc(self, x):
        if x == '?':
            return x
        self._ent = None
        self.n = self.n+1
        old = self.counts.get(x,0) 
        new = old and old+1 or 1 # what is this ??
        self.counts[x] = new
        if new > self.most:
            self.most, self.mode = new, x

        return x

    def symDec(self, x):
        self._ent = None
        self.n = self.n -1
        self.counts[x] = self.counts[x] - 1
        return x

    def symEnt(self):
        if self._ent == None:
            self._ent = 0
            p = 0
            for k,v in self.counts.items():
                p = v / self.n
                self._ent = self._ent - p*math.log(p,2)

        return self._ent


