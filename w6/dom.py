import re, sys, random, math
from num import Num
from sym import Sym
from rows import Rows, rows
from test import O


def another(r, rows):
    val = max(0, math.floor(0.5 + random.random()*len(rows)) - 1) 
    if not r == val:
    	return rows[val]
    return another(r, rows)

def dom(t, row1, row2):
    s1 = 0
    s2 = 0
    n = len(t.w)
    for c, w in t.w.items():
        a0 = row1[c]
        b0 = row2[c]
        a = t.nums[c].numNorm(a0)
        b = t.nums[c].numNorm(b0)
        s1 = s1 - 10 ** (w * (a-b)/n)
        s2 = s2 - 10 ** (w * (b-a)/n)
    return s1/n < s2/n

def dump(rows):
    for row in rows:
        row[len(row)-1] = str("%.2f"%row[len(row)-1])
        # print("\t".join(str(r) for r in row))
        
def doms(t):
    n = 100
    c = len(t.name)
    # print("\t"+ str(t.name) +"\t"+">dom")
    for r1, row1 in enumerate(t.rows):
        row1.append(0)
        for i in range(n):
            row2 = another(r1, t.rows)
            s = dom(t, row1, row2) and 1/n or 0
            row1[c] = row1[c] + s
    dump(t.rows)
    return t

def mainDom(file):
    doms(rows(file))

# @O.k
# def test1():
#     random.seed(1)
#     print("\nweatherLong.csv\n")
#     mainDom("weatherLong.csv")

# @O.k
# def test2():
#     random.seed(1)
#     print("\nauto.csv\n")
#     mainDom("auto.csv")
