import math

class Sym:
    def __init__(self):
        self.counts=[]
        self.mode = None
        self.most = 0
        self.n = 0
        self._ent = None

    def syms(self, f):
        f = f if f else lambda x: x
        for x in self.counts:
            self.symInc(f(x))
        return

    def syncInc(self, x):
        if x == ?:
            return x
        self._ent = None
        t.n = t.n+1
        old = self.counts[x] # no check for x ?
        new = old and old+1 or 1
        t.counts[x] = new
        if new > t.most:
            t.most, t,mode = new, x

        return x

    def symDec(self, x):
        self._ent = None
        t.n = t.n -1
        #i.counts[x] = i.counts - 1
        return x

    def symEnt(self):
        if not self._ent:
            self._ent = 0
        for x,n in enumerate(self.counts):
            p = n / self.n
            self._ent = self._ent - p*math.log(p,2)

        return self._ent


