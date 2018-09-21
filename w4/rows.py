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
        for idx,col in enumerate(self._use):
            x = cells[col]
            if not "?" in x:
                if self.nums.get(col) is not None:
                    x = float(x)
                    self.nums.get(col).numInc(x)
                else:
                    self.syms.get(col).symInc(x)
            #l.append(x)
            self.rows[r].append(x)

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

