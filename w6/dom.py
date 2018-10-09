from Num import Num
from rows import Data
from Sym import Sym

class Dom:
    #@staticmethod
    def dom(self,row1,row2, data):
        s1,s2,n = 0,0,0
        n=len(data.name)

        for c,w in data.w.items():
            a0= row1[c-1]
            b0= row2[c-1]
            a= data.nums[c].numNorm(a0)
            b= data.nums[c].numNorm(b0)
            s1 = s1 - pow(10,(w * (a-b)/n))
            s2 = s2 - pow(10,(w * (b-a)/n))
        return s1/n < s2/n

    #@staticmethod
    def doms(self,data : Data):
        n= 100
        c= len(data.name)
        data.name[c] = ">dom"
        for r1 in range(0,len(data.rows)):
            row1 = data.rows[r1]
            row1.append(0)
            for s in range(0,n):
                row2 =data.another(r1)
                s = self.dom(row1,row2, data) and 1/n or 0
                #k = round(s,2)
                row1[c] = row1[c] + s
            data.rows[r1]=row1
            data.rows[r1][-1]=round(data.rows[r1][-1], 2)
        return data



