
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

    print("\t\t n  mod  freq\n")
    for k,v in s.items():
        print(str(k) + " "+ str(t.name[k]) + " " + str(v.n) + " " + str(v.mode) + " " + str(v.most))

    assert len(s) == 3 # after parsing data set sym = 3

    # from list of sys get 1 value and check for most and mode
    s1 = s.get(1)
    assert (s1.mode == "sunny" and s1.most == 5)

    print("\n\n\t\tn  mu  sd\n")
    for k,v in n.items():
        print(str(k) + " "+ str(t.name[k]) + " " + str(v.n) + " " + str(round(v.mu,2)) + " " + str(round(v.sd,2)))

    # from list of nums get 1 value and check mu and sd
    assert len(n) == 1 # #num = 1
    n1 = n.get(2)
    assert ((73.57 == round(n1.mu,2)) and (6.57 == round(n1.sd,2)))


@O.k
def testing_weatherLong():
    t = Data()
    t = t.read("../data/weatherLong.csv")
    s = t.syms
    n = t.nums

    print("\t\tn  mod  freq\n")
    for k,v in s.items():
        print(str(k) + " "+ str(t.name[k]) + " " + str(v.n) + " " + str(v.mode) + " " + str(v.most))

    assert len(s) == 3 #should have 3 symbolic values
    s1 = s.get(1)
    assert (s1.mode == "sunny" and s1.most == 10)

    print("\n\n\t\tn  mu  sd\n")
    for k,v in n.items():
        print(str(k) + " "+ str(t.name[k]) + " " + str(v.n) + " " + str(round(v.mu,2)) + " " + str(round(v.sd,2)))

    assert len(n) == 2 #should have 2 numeric values
    n1 = n.get(3)
    assert ((81.64 == round(n1.mu, 2)) and (10.09 == round(n1.sd, 2)))


@O.k
def testing_auto():
    t = Data()
    t = t.read("../data/auto.csv")
    s = t.syms
    n = t.nums

    print("\t\tn  mod  freq\n")
    for k,v in s.items():
        print(str(k) + " "+ str(t.name[k]) + " " + str(v.n) + " " + str(v.mode) + " " + str(v.most))

    assert len(s) == 2 # sym = 2
    s1 = s.get(1)
    assert (s1.mode == "4" and s1.most == 204)


    print("\n\n\t\tn  mu  sd\n")
    for k,v in n.items():
        print(str(k) + " "+ str(t.name[k]) + " " + str(v.n) + " " + str(round(v.mu,2)) + " " + str(round(v.sd,2)))

    assert len(n)==6 #num = 6
    n1 = n.get(3)
    assert ((104.47 == round(n1.mu, 2)) and (38.49 == round(n1.sd, 2)))


if __name__== "__main__":
  O.report()
