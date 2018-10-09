from w5.dom import Dom
from w5.rows import Data
from w5.testingModule import O
from w6.super import *
from w5.Num import Num

@O.k
def test_sup():
    d = Data()
    d.rows1("data/weatherLong.csv")
    sup_disc(d)

if __name__== "__main__":
  O.report()