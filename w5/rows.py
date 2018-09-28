from Sym import Sym
from Num import Num
import re
import random

class Data:
    def __init__(self):
        self.w = {}
        self.syms = {}
        self.nums = {}
        self.c = None
        self.rows = {}
        self.name = {}
        self._use = {}
        self.indeps = []

    """def indep(self, c):
    return not in self.w[c] and self.c is not c

        def dep(self, c):
    return not indep(c)
    """

    def header(self, cells):
        for i,col in enumerate(cells):
            if not re.match('\?', col):
                c = len(self._use)+1
                self._use[c] = i
                self.name[c] = col
                if re.match("[<>$]",col): #check for pattern
                    self.nums[c] = Num()
                else:
                    self.syms[c] = Sym()
                if  re.match("<",col) :
                    self.w[c]  = -1
                elif re.match(">",col):
                    self.w[c]  =  1
                elif re.match("!", col):
                    self.c =  c 
                else:
                    self.indeps.append(c)


    def row(self,cells):
        r= len(self.rows)
        self.rows[r] = []
        for idx,col in self._use.items():
            x = cells[col]
            if not "?" in x:
                if self.nums.get(idx) is not None:
                    x = float(x)
                    self.nums.get(idx).numInc(x)
                else:
                    self.syms.get(idx).symInc(x)
            #l.append(x)
            self.rows[r].append(x)

    def rows1(self, fname):
        with open(fname) as stream:
            first,lines = True, stream.readlines()
            for line in lines: 
                re.sub("[\t\r ]*","",line)
                re.sub("#.*","",line)
                c = line.split(",")
                cells = [x.strip() for x in c]
                if len(cells) > 0:
                    if first:
                        t = self.header(cells) 
                    else: 
                        t = self.row(cells)
                first = False

    def read(self, f):
        self.rows1(f)
        return self


    def another(self, row):
        r = random.randrange(0, len(self.rows))
        if row == r:
            return self.another(row)
        return self.rows[r]

