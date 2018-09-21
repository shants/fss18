
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


from rows import Data

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
def testing_weather():
    t = Data()
    t = t.read("../data/weather.csv")
    s = t.syms
    n = t.nums

    print("symbolic ")
    for k,v in s.items():
        print(str(k) + " "+ str(t.name[k]) + " " + str(v.n) + " " + str(v.mode) + " " + str(v.most))

    print("numeric")
    for k,v in n.items():
        print(str(k) + " "+ str(t.name[k]) + " " + str(v.n) + " " + str(round(v.mu,2)) + " " + str(round(v.sd,2)))





if __name__== "__main__":
  O.report()
