from w5.Num import Num
import math
#from .tests.testingModule import O
from w5.rows import Data

from operator import itemgetter


def ksort(r, k):
  r = sorted(r, key=lambda r1: r1[k])
  return r

def dump(a, sep="\t"):
  for i in a:
    print(sep.join(str(b) for b in i))


def super(data):

  rows   = data.rows
  goal   = len(rows[0])-1
  enough = len(rows)**.05

#-- -------------------------------------------
#-- This generates a print string for a band
#-- that streches from `lo` to `hi`.


  def band(c,lo,hi):
    if lo==0:
      return ".." + str(rows[hi][c])
    elif hi == most:
      return str(rows[lo][c]) + ".."
    else:
      return str(rows[lo][c]) +".." + str(rows[hi][c])

  #-- Find one best cut, as follows.
  #--
  #-- - First all everything to a _right_ counter
  #--   (abbreviated here as `r`).
  #-- - Then work from `lo` to `hi` taking away
  #--   values from the _right_ and adding them
  #--   to a _left_ counter (abbreviated here as `l`).
  #-- - Using the information in these _right_ and
  #--   _left_ counters, work out where the best `cut` is.
  #-- - If no such `cut` found, return `nil`.
  #--
  #-- Tehcnical note: actually, we run two _right_
  #-- and two _left_ counters:
  #--
  #-- - two for the independent column (`xl` and `xr`)
  #-- - and two for the goal column  (`yl` and `yr`)

  def argmin(c,lo,hi):
      xl,xr = Num(), Num()
      yl,yr = Num(), Num()
      for i in range(lo,hi+1):
        xr.numInc(rows[i][c])
        yr.numInc(rows[i][goal])

      bestx = xr.sd
      besty = yr.sd
      mu    = yr.mu
      if (hi - lo > 2*enough):
        for i in range(lo,hi+1):
          x = rows[i][c]
          y = rows[i][goal]
          xl.numInc(x); xr.numInc(x)
          yl.numInc(y); yr.numDec(y)
          if xl.n >= enough and xr.n >= enough:
            tmpx = xl.numXpect(xr) * 1.05
            tmpy = yl.numXpect(yr) * 1.05
            if tmpx < bestx:
              if tmpy < besty:
                cut,bestx,besty = i, tmpx, tmpy

      return cut,mu

  #-- If we can find one good cut:
  #--
  #-- - Then recurse to, maybe, find other cuts.
  #-- - Else, rewrite all values in `lo` to `hi` to
  #--   the same string `s` representing the range..

  def cuts(c,lo,hi,pre):
    txt = pre + str(rows[lo][c]) + ".." + str(rows[hi][c])
    cut,mu = argmin(c,lo,hi)
    if cut:
      print(txt)
      cuts(c,lo,   cut, pre + "|.. ")
      cuts(c,cut+1, hi, pre+"|.. ")
    else:
      s = band(c,lo,hi)
      print(txt+" ==> "+str(math.floor(100*mu)))
      for r in range(lo,hi+1):
          rows[r][c]=s


  #-- Our data sorts such that all the "?" unknown values
  #-- are pushed to the end. This function tells us
  #-- where to stop so we don't run into those values.

  def stop(c,t):
    for i in range(len(t),0,-1):
      if t[i][c] != "?":
        return i
    return 0

  #-- For all numeric indpendent columns, sort it and
  #-- try to cut it. Then `dump` the results to standard output.

  for _,c in enumerate(data.indeps):
    if data.nums[c]:
      ksort(c,rows) #-- sorts the rows on column `c`.
      most = stop(c,rows)
      print("\n-- " + data.name[c] + " ----------")
      cuts(c,1,most,"|.. ")
      print(", ".join(data.name.values()).replace("$", "")) #-- dump dollars since no more nums
      dump(rows)


  #-- Main function, if this is called top-level.

