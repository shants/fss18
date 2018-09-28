from .Num import Num
from .rows import Data
from .Sym import Sym


class Dom:
    def dom(self,row1,row2, data):
        s1,s2,n = 0,0,0
        n=len()

        for c,w in self.w.items():
            a0= row1[c-1]
            b0= row2[c-1]
            a= data.nums[c].numNorm(a0)
            b= data.nums[c].numNorm(b0)
            s1 = s1 - 10^(w * (a-b)/n)
            s2 = s2 - 10^(w * (b-a)/n)
        return s1/n < s2/n

    def doms(self,data : Data):
        n= 100
        c= len(data.name)+1
        data.name[c] = ">dom"
        for r1 in range(1,len(data.rows)):
            row1 = data.rows[r1]
            row1.append(0)
            for s in range(1,n+1):
                row2 =0#= data(r1,t.rows)
                s = self.dom(row1,row2) and 1/n or 0
                row1[c-1] += + s
            data.rows[r1]
        return data


