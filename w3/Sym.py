
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

