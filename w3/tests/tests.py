#ACK Did refer to code https://github.com/FahmidMorshed/fss18/tree/master/Week%203
# Once or twice to get doubt cleared, did not copy 
import testingModule
#from .. import Sample
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from Sample import Sample
from Sym import Sym
from Num import Num
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
    s1 = Sym()

    s1 = s1.syms([ 'y','y','y','y','y','y','y','y','y', 'n','n','n','n','n'])
    print(s1.symEnt())
    assert  round(s1.symEnt(),4) ==  0.9403
    #assert 1 == 1


@O.k
def testing_Num():
    n1 = Num()
    n1 = n1.nums([ 4,10,15,38,54,57,62,83,100,100,174,190,215,225,
       233,250,260,270,299,300,306,333,350,375,443,475,
       525,583,780,1000])

    print(n1.mu, n1.sd)
    assert(n1.mu == 270.3 )
    assert(round(n1.sd,3) == 231.946)
    

if __name__== "__main__":
  O.report()
