import testingModule
#from .. import Sample
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import Sample
from testingModule import O


@O.k
def testing_Sample():
  assert 1 == 1


@O.k
def testing_Sym():
    assert 1 == 1

@O.k
def testing_Num():
    assert 1 == 1


if __name__== "__main__":
  O.report()
