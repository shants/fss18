from num import Num
from sym import Sym
from test import O
import re, sys

class Rows:
    
    def __init__(self):
        self.w = {}
        self.syms = {}
        self.nums = {}
        self._class = None
        self.rows = []
        self.name = []
        self._use = []
        self.indeps = []

    def indep(self, c):
        return not c in self.w and self._class!=c

    def dep(self, c):
        return not self.indep(c)

    def header(self,cells):
        # self = self or Rows()
        # self.indep = []
        for c0,x in enumerate(cells):
            if not "?" in x:
                c = len(self._use)
                self._use.append(c0)
                self.name.append(x)
        
                if "$" in x or "<" in x or ">" in x:
                    self.nums[c] = Num([])
                else:
                	self.syms[c] = Sym([])

                if "<" in x:
                    self.w[c] = -1
                elif ">" in x:
                    self.w[c] = 1
                elif "!" in x:
                    self._class = c
                else:
                    self.indeps.append(c)
        return self

    '''
    Processing each row and 
    deciding when to skip a value
    '''
    def row(self, cells):
        r = len(self.rows)
        self.rows.append([])
        for c, c0 in enumerate(self._use):
            x = cells[c0]
            if x!="?":
                if c in self.nums:
                    x = round(float(x),2)
                    self.nums[c].numInc(x)
                else:
                    self.syms[c].symInc(x)
            self.rows[r].append(x)
        return self

def splitLines(text = None):
	#check if the file has .csv extension
    if text[-3:] in ["csv",".dat"]:
    	with open(text) as file:
    		for line in file:
    			yield line
    #reading input stream data if no file is passed
    elif text == None:
    	for line in sys.stdin:
    		yield line
    else:
    	for line in text.splitlines():
    		yield line

def rows1(stream):
	#Creating an object of type Rows()
    line = Rows()
    first = True
    for line1 in stream:
        line1 = re.sub(r'([\n\r\t]|#.*)', "", line1)
        cells = line1.split(",")
        if len(cells)>0 and cells[0] != "" :
            if first :
                line.header(cells)
            else :
                line.row(cells)
            first=False
    return line

def rows(src):
    return rows1(splitLines(src))