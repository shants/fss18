from Sym import Sym
from Num import Num

class Data:
    def __init__(self):
        self.w = {}
        self.syms = {}
        self.nums = {}
        self.c = None
        self.rows = {}
        self.name = {}
        self._use = {}

    def indep(self, c):
        #return not self.w[c] and self.c # check for t.w[c] and t.class ~= c

    def dep(self, c):
        return not indep(c)

    def header(self, cells):
        t = data()
        t.indeps = {}
        for c0,x in enumerate(cells):
            if "%?" not in x:
                c = len(t._use)+1
                t._use[c] = c0
                t.name[c] = x
                if "<>%$" in x: #check for pattern
                    t.nums[c] = Num()
                else:
                    t.syms[c] = Sym()
                
                if  "<" in x:
                    t.w[c]  = -1
                elif ">" in x:
                    t.w[c]  =  1
                elif "!" in x:
                    t.c =  c 
                else:
                    t.indeps[len(t.indeps)+1] = c
        return t

    


    def row(self,cells):
        r= len(self.rows)+1
        self.rows[r] = {}
        for c,c0 in enumerate(self._use):
            x = cells[c0]
            if x != "?":
                if t.nums[c]:
	            x = tonumber(x)
                    numInc(t.nums[c], x)
                else
	            symInc(t.syms[c], x)
            t.rows[r][c] = x 
        return t


    def rows1(stream, t,f0,f):
        first,line = true,io.read()
        while line do
            line= line:gsub("[\t\r ]*","")
            :gsub("#.*","")
            cells = split(line)
            line = io.read()
            if #cells > 0 then
                if first then
                    f0(cells,t) 
                else 
                    f(t,cells)
            first = false
        io.close(stream)
        return t

    def rows(file,t,f0,f):
        return rows1( file and io.input(file) or io.input(),
                t  or data(), f0 or header, f or row) 

