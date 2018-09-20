from Sym import Sym
from Num import Num
import re

class Data:
    def __init__(self):
        self.w = {}
        self.syms = {}
        self.nums = {}
        self.c = None
        self.rows = []
        self.name = {}
        self._use = {}
        self.indeps = []

    """def indep(self, c):
        return not in self.w[c] and self.c is not c

           def dep(self, c):
        return not indep(c)
    """

    def header(self, cells):
        for c0,x in enumerate(cells):
            if not re.match("%?",x):
                c = len(self._use)+1
                self._use[c] = c0
                self.name[c] = x
                if re.match("<>%$",x): #check for pattern
                    self.nums[c] = Num()
                else:
                    self.syms[c] = Sym()
                
                if  re.match("<",x) :
                    self.w[c]  = -1
                elif re.match(">",x):
                    self.w[c]  =  1
                elif re.match("!", x):
                    self.c =  c 
                else:
                    self.indeps.append(c)


    def row(self,cells):
        r= len(self.rows)+1
        l = []
        for c,c0 in enumerate(self._use):
            x = cells[c0]
            if not "?" in x:
                if self.nums[c]:
                    x = int(x)
                    self.nums[c].numInc(x)
                else:
                    self.syms[c].symInc(x)
            l.append(x)
            self.rows[r]= l 

    def rows1(self, fname):
        with open(fname) as stream:
            first,lines = True, stream.readlines()
            for line in lines: 
                re.sub("[\t\r ]*","",line)
                re.sub("#.*","",line)
                cells = line.split(",")
                if len(cells) > 0:
                    if first:
                        t = self.header(cells) 
                    else: 
                        t = self.row(cells)
                first = False

    def read(self, f):
        self.rows1(f)
        return self

