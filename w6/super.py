from testingModule import O
from Num import Num
from Sym import Sym
from dom import dom, doms
from rows import Rows, rows
import re, sys, math, random


def split(splitData):
  sum = 0
  result = 0
  listItems = splitData.items()
  for _, (n, sd) in listItems:
    sum += n
  for _, (n, sd) in listItems:
    result += n / (sum + math.pow(10, -32)) * sd
  return result


def ksort(k, t):
  t = sorted(t, key=lambda x: str(x[k]))
  return t


def dump(row):
  for data in row:
    print("\t".join(str(char) for char in data))


# parameters values from config.lua
super_enough = 0.5
super_margin = 1.05


def super(data, goal=None, enough=None):
  splitData = {}
  # print(type(data))
  rows = data.rows
  if goal == None:
    goal = len(rows[0]) - 1
  if enough == None:
    enough = len(rows) ** super_enough

  # goal = goal if goal not None else len(rows[0]-1)
  # enough = enough if enough not None else len(rows)**super_enough

  def band(c, lo, hi):
    if lo == 1:
      return ".." + str(rows[hi][lo])
    elif hi == most:
      return str(rows[lo][c]) + ".."
    else:
      return str(rows[lo][c]) + ".." + str(rows[hi][c])

  def argmin(c, lo, hi):
    cut = None
    xl = Num([])
    xr = Num([])

    yl = Num([])
    yr = Num([])

    for i in range(lo, hi + 1):
      xr.numInc(rows[i][c])
      yr.numInc(rows[i][goal])
    bestx = xr.sd
    besty = yr.sd
    mu = yr.mu
    n = yr.n

    if (hi - lo) > 2 * enough:
      for i in range(lo, hi + 1):
        x = rows[i][c]
        y = rows[i][goal]
        xl.numInc(x)
        xr.numInc(x)
        yl.numInc(y)
        yr.numInc(y)

        if xl.n >= enough and xr.n >= enough:
          tmpx = Num.numXpect(data, xl, xr) * super_margin
          tmpy = Num.numXpect(data, yl, yr) * super_margin
          if tmpx < bestx and tmpy < besty:
            cut, bestx, besty = i, tmpx, tmpy
    return (cut, mu, n, besty)

  def cuts(c, lo, hi, pre):
    txt = pre + str(rows[lo][c]) + ".." + str(rows[hi][c])
    cut, mu, n, sd = argmin(c, lo, hi)
    if cut:
      print(txt)
      cuts(c, lo, cut, pre + "|.. ")
      cuts(c, cut + 1, hi, pre + "|.. ")
    else:
      s = band(c, lo, hi)
      splitData[c] = {}
      splitData[c][s] = (n, sd)
      print(txt + "==>" + str(math.floor(100 * mu)))
      for r in range(lo, hi + 1):
        rows[r][c] = s

  def stop(c, t):
    for i in range(len(t) - 1, -1, -1):
      if t[i][c] != '?':
        return i
    return 0

  for c in data.indeps:
    if c in data.nums:
      rows = ksort(c, rows)
      most = stop(c, rows)
      print("\n--" + data.name[c] + "-------")
      cuts(c, 1, most, "|.. ")
  print(" ".join(str("%10s" % e) for e in data.name).replace(",", ""))
  dump(rows)

  splitter = None
  min_sd = sys.maxsize
  for idx in data.indeps:
    if idx in data.nums:
      cur_sd = split(splitData[idx])
      if cur_sd < min_sd:
        min_sd = cur_sd
        splitter = data.name[idx]
  print("Splitter attrbute is ", splitter)
  print("Expected standard deviation is ", min_sd, "\n")


def wrapperSuper(s):
  super(doms(rows(s)))


@O.k
def testingSuper():
  print("\nFor weatherLong.csv")
  wrapperSuper('data\weatherLong.csv')

  print("\nFor auto.csv")
  wrapperSuper('data\auto.csv')