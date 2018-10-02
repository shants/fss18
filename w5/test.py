#from .testingModule import O
from w5.dom import Dom
from w5.rows import Data
from w5.testingModule import O
from w5.unsuper import *

@O.k
def test_weather():
    d = Dom()
    dt = Data()
    dt = dt.read("data/weatherLong.csv")
    d2 = d.doms(dt)
    for i in d2.rows:
        print(i)
    assert 1 == 1

@O.k
def test_auto():
    d = Dom()
    dt = Data()
    dt = dt.read("data/auto.csv")
    d2 = d.doms(dt)
    for i in d2.rows:
        print(i)

    assert 1 == 1

@O.k
def test_unsup():
    d = Data()
    d.rows1("data/weatherLong.csv")
    unsuper(d)

if __name__== "__main__":
  O.report()