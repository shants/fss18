#from .testingModule import O
from dom import Dom
from rows import Data
import re
import traceback
class O:
  y=n=0
  @staticmethod
  def report():
    print("\n# pass= %s fail= %s %%pass = %s%%"  % (
          O.y,O.n, int(round(O.y*100/(O.y+O.n+0.001)))))
  @staticmethod
  def k(f):
    try:
      print("\n-----| %s |-----------------------" % f.__name__)
      if f.__doc__:
        print("# "+ re.sub(r'\n[ \t]*',"\n# ",f.__doc__))
      f()
      print("# pass")
      O.y += 1
    except:
      O.n += 1
      print(traceback.format_exc())
    return f





@O.k
def test_weather():
    d = Dom()
    dt = Data()
    dt = dt.read("weatherLong.csv")
    d2 = d.doms(dt)
    assert 1 == 1

@O.k
def test_auto():
    assert 1 == 1


if __name__== "__main__":
  O.report()