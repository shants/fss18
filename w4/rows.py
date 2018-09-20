from Sym import Sym
from Num import Num
import re

class Data:
    def __init__(self):
        self.w = {}
        self.syms = {}
        self.nums = {}
        self.c = None
        self.rows = {}
        self.name = {}
        self._use = []
        self.indeps = []

    def indep(self, c):
        return not in self.w[c] and self.c is not c

    def dep(self, c):
        return not indep(c)

    def header(self, cells):
        t = data()
        #t.indeps = {}
        for c0,x in enumerate(cells):
            if not re.match("%?",x):
                c = len(t._use)+1
                t._use[c] = c0
                t.name[c] = x
                if re.match("<>%$",x): #check for pattern
                    t.nums[c] = Num()
                else:
                    t.syms[c] = Sym()
                
                if  re.match("<",x) x:
                    t.w[c]  = -1
                elif re.match(">",x):
                    t.w[c]  =  1
                elif re.match("!", x):
                    t.c =  c 
                else:
                    t.indeps.append(c)
        return t

    


    def row(self,cells):
        r= len(self.rows)+1
        self.rows[r] = {}
        for c,c0 in enumerate(self._use):
            x = cells[c0]
            if x != "?":
                if self.nums[c]:
	            x = int(x)
                    numInc(self.nums[c], x)
                else
	            symInc(self.syms[c], x)
            self.rows[r][c] = x 
        #return self


    def rows1(fname):
        with open(fname) as stream

        first,lines = true, stream.readlines()
        for line in lines: 
            re.sub("[\t\r ]*","",line)
            re.sub("#.*","",line)
            cells = line.split(",")
            if len(cells) > 0:
                if first then
                    f0(cells,t) 
                else 
                    f(t,cells)
            first = false
        return t

    def rows(f):
        return rows1(f)

