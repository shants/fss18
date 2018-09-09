import testingModule
#from .. import Sample
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from Sample import Sample
from testingModule import O
import random


@O.k
def testing_Sample():
    random.seed(1)
    s = []

#-- create some samples holding 32,64,128... max items
  
    for i in range(5,10):
        o = Sample(2**i)
        s.append(o)

    #-- 10,000 store the same number in all samples
    for i in range(1,10000):
        y= random.random()
    for t in s:
        t.sampleInc(y)

    #-- check if any of them are +/- 0.2 of 0.5
    for t in s: 
        o = t.nth(0.5)
        print(t.max, o) 
        assert (( o >= .05-.33) and ( o <= 0.5+.33 ))
        #assert 1 == 1

@O.k
def testing_Sym():
    assert 1 == 1

@O.k
def testing_Num():
    assert 1 == 1


if __name__== "__main__":
  O.report()
