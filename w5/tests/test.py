#from .testingModule import O
from dom import Dom
from rows import Data
from testingModule import O

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