import lib_fss
from Num import Num
import math

class Unsuper:
    def __init__(self, data,enough=2):
        self.rows = data.rows
        self.enough = pow(len(self.rows),0.5)

    def band(self,c,lo,hi):
        if lo==1:
            return ".." + str(self.rows[hi][c])
        elif hi == most:
            return str(self.rows[lo][c]) + ".."
        else:
            return str(self.rows[lo][c]) + ".." + str(self.rows[hi][c])

    def argmin(self, c,lo,hi):
        if (hi - lo > 2*self.enough):
            l,r = Num(), Num()
            for i in range(lo,hi):
                r.numInc(self.rows[i][c])
            best = r.sd
            for i in range(lo,hi):
                x = self.rows[i][c]
                l.numInc(x)
                r.numDec(x)
                if l.n >= self.enough and r.n >= self.enough:
                    tmp = l.numXpect(l,r) * 1.05
                if tmp < best:
                    cut,best = i, tmp
        return cut


    def cuts(self,c,lo,hi,pre):
        txt = pre + str(self.rows[lo][c]) + ".. " + str(self.rows[hi][c])
        cut = self.argmin(c,lo,hi)
        if cut:
            fyi(txt)
            self.cuts(c,lo,   cut, pre + "|.. ")
            self.cuts(c,cut+1, hi, pre + "|.. ")
        else:
            b= self.band(c,lo,hi)
            fyi(txt +" ("+str(b)+")")
            for r in range(lo,hi):
                self.rows[r][c]=b

    def stop(self,c,t):
        for i in range(len(t),1,-1):
            if t[i][c] != "?":
                return i
        return 0

    for _,c  in enumerate(self.data.indeps) do
        if data.nums[c] then
            ksort(c,rows)
            most = stop(c,rows)
            fyi("\n-- ".. data.name[c] .. most .. "----------")
            cuts(c,1,most,"|.. ") end end
            print(gsub( cat(data.name,", "), "%$",""))
            dump(rows)


if __name__ == "__main__":
    unsuper(rows())
