import re,traceback
import re as regex
from collections import defaultdict
from collections import Counter
import random

from testingModule import O

def double(x):
  return x*2    

def sumAndproduct(x=0,y=0):
  return (x+y,x*y)

"""
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
"""

@O.k
def testingSucess_WhiteSpace():
  ans = 1 in [1,2,3,4,5]
  assert ans == True

@O.k
def testingSuccess_Module():
  p = regex.compile('[a-z]+',regex.I)
  ans = p.match("test")
  assert ans != None

@O.k
def testingSuccess_division():
  ans = 5 /2
  assert ans == 2.5

@O.k
def testingSuccess_function2x():
  assert double(4)==8

@O.k
def testingSucess_Strings():
  s = "Hello"
  assert  len(s) == 5

@O.k
def testingSucess_ExceptionHandling():
  flag = False
  try:
    0/0
  except ZeroDivisionError:
    flag = True

  assert flag == True

@O.k
def testingSucess_Lists():
  l = range(5)
  assert len(l) == 5
  assert l[4]==l[-1]

@O.k
def testingSucess_Unpack():
  l = [1,2]
  a,b = l
  assert a == 1 and b == 2

@O.k
def testingSucess_Tuple():
  (a,b) = sumAndproduct(2,3)
  assert a == 5 and b == 6

@O.k
def testingSucess_Dictionary():
  hash = {}
  hash["student1"]=20
  assert hash.get("student1",0)==20 and hash.get("student2",0)==0

@O.k
def testingSuccess_Defaultdictionary():
  words = "First Assignment on First day of fss18".split(" ")
  wordcount = defaultdict(int)
  for w in words:
    wordcount[w]=wordcount[w]+1
  
  assert wordcount["First"]==2 and wordcount["day"]==1 and wordcount["random"]==0

@O.k
def testingSucess_Counter():
  c = Counter([0,1,1,1,1,2,2,3])
  l = c.most_common(1)
  a,_ = l[0]
  assert a == 1

@O.k
def testingSuccess_Set():
  l = [1, 2, 3, 1, 2, 3]
  s = set(l)
  assert len(s) == 3

@O.k
def testingSuccess_Loop():
  x = 0 
  while x < 10:
    x += 1
  assert x == 10

@O.k
def testingSuccess_TrueFalse():
  x = 1 < 2
  assert x == True


@O.k
def testingSuccess_All():
  x = all([True, 1, { 3 }]) 
  assert x == True

@O.k
def testingSuccess_Sort():
  x = [4,1,2,3] 
  y = sorted(x)
  assert y[0] == 1
  x.sort()
  assert x[0] == 1

@O.k
def testingSuccess_ListComprehension():
  squares      = [x * x for x in range(5)] 
  assert squares[2] == 4

def createGenerator():
  
  for i in [5,10]:
    yield i*i

@O.k
def testingSuccess_Generator():
  a = createGenerator()
  sum = 0
  for i  in  a:
    sum = sum + i  
  assert sum == 125

@O.k
def testingSuccess_Random():
  x = random.randrange(3, 6)
  assert x >= 3 and x <6 

@O.k
def testingSuccess_Regex():
   ans = regex.search("a", "cat")
  
   assert ans is not None


class MySet:
  def __init__(self, values = None):
    self.dict = {}
    if values is not None:
      for v in values:
        self.add(v)

  def __repr__(self):
    return "MySet: " + str(self.dict.keys())

  def add(self, value):
    self.dict[value] = True

  def contains(self, value):
    return value in self.dict

  def remove(self, value):
    del self.dict[value]
 
@O.k
def testingSuccess_Class():
  s = MySet([1,2,4])
  assert s.contains(2) == True

@O.k
def testingSuccess_Function():
  l = [1, 2, 3, 4] 
  x = list(map(lambda a : a*2,l))
  x1 = list(filter(lambda e : e%2!=0,x))
  assert x[0]==2 and len(x1) == 0

@O.k
def testingSuccess_Enumerate():
  l = [0,1,2,3]
  ans = True
  for idx,val in enumerate(l):
    if( idx != val):
      ans = False

  assert ans == True  

@O.k
def testingSuccess_Zip():
  list1 = ['a', 'b', 'c'] 
  list2 = [1, 2, 3] 
  l = list(zip(list1, list2))
  a,b = l[0]
  assert a == 'a' and b == 1

def doubler(f):    
  def g(x):        
    return 2 * f(x)    
  return g

def f1(x):    
  return x + 1

@O.k
def testingSuccess_FunctionAsParam():
  g = doubler(f1) 
  a = g(3)
  assert a == 8

def multiarg(*argc, **kwargs):
  return len(argc), len(kwargs)

@O.k
def testingSuccess_MultipleArgs():
  a,b = multiarg(1,2,3,key1="word1",key2="word2")
  assert a==3 and b == 2
  
if __name__== "__main__":
  O.report()
