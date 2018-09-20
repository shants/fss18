import testingModule

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


from rows import Data
from testingModule import O


@O.k
def testing_Data():
    t = Data()
    t = t.read("../data/weather.csv")
    s = t.syms
    n = t.nums

    for k,v in enumerate(s):
        print(t.name[c] + " " + str(v))

    for k,v in enumerate(n):
        print(t.name[c] + " " + str(v))



if __name__== "__main__":
  O.report()
