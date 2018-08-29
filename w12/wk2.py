from testingModule import O

DATA1 ="""
outlook,$temp,?humidity,windy,play
sunny,85,85,FALSE,no
sunny,80,90,TRUE,no
overcast,83,86,FALSE,yes
rainy,70,96,FALSE,yes
rainy,68,80,FALSE,yes
rainy,65,70,TRUE,no
overcast,64,65,TRUE,yes
sunny,72,95,FALSE,no
sunny,69,70,FALSE,yes
rainy,75,80,FALSE,yes
sunny,75,70,TRUE,yes
overcast,100,25,90,TRUE,yes
overcast,81,75,FALSE,yes
rainy,71,91,TRUE,no"""

DATA2 ="""
    outlook,   # weather forecast.
    $temp,     # degrees farenheit
    ?humidity, # relative humidity
    windy,     # wind is high
    play       # yes,no
    sunny,85,85,FALSE,no
    sunny,80,90,TRUE,no
    overcast,83,86,FALSE,yes

    rainy,70,96,FALSE,yes
    rainy,68,80,FALSE,yes
    rainy,65,70,TRUE,no
    overcast,64,

                  65,TRUE,yes
    sunny,72,95,FALSE,no
    sunny,69,70,FALSE,yes
    rainy,75,80,FALSE,yes
          sunny,
                75,70,TRUE,yes
    overcast,100,25,90,TRUE,yes
    overcast,81,75,FALSE,yes # unique day
    rainy,71,91,TRUE,no"""



def lines(s):
  "Return contents, one line at a time."
  #https://stackoverflow.com/questions/761804/how-do-i-trim-whitespace-from-a-python-string
  #https://stackoverflow.com/questions/15422144/how-to-read-a-long-multiline-string-line-by-line-in-python
  return s.splitlines()

def removeComments(s):
  l = s.split("#")
  a = l[0].strip()
  return a

def rows(src):
  """Kill bad characters. If line ends in ',' 
   then join to next. Skip blank lines."""
   #https://stackoverflow.com/questions/19954593/python-checking-a-strings-first-and-last-character
  i = 0
  src = list(map(removeComments,src)) 
  src = [x for x in src if x]
  while (i<len(src)-1):
    if src[i].endswith(",") :
      src[i]=src[i] + src[i+1]
      del src[i+1]
    else:
      i=i+1
  
  assert i == len(src)-1
  if src[i].endswith(","):
    print("Last line ends with , !! What to do")
  return src

def cols(src):
  """ If a column name on row1 contains '?', 
  then skip over that column."""
  #https://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method
  src = [i.split(",") for i in src]
  colToSkip = set()
  
  for idx,ch in enumerate(src[0]):
    if "?" in ch:
      colToSkip.add(idx)
  
  for rows in src:
    for c in colToSkip:
      del rows[c]
  
  return src

  

def prep(src):
  """ If a column name on row1 contains '$', 
  coerce strings in that column to a float."""
  # conversion check from https://www.datacamp.com/community/tutorials/python-data-type-conversion
  toFloat = set()
  for idx,ch in enumerate(src[0]):
    if "$" in ch:
      toFloat.add(idx)

  for rows in src[1:]:
    for c in toFloat:
      rows[c]=float(rows[c])
  
  return src


def ok0(s):
  for row in prep(cols(rows(lines(s)))):
    print(row)

@O.k
def ok1(): ok0(DATA1)

@O.k
def ok2(): ok0(DATA2)

if __name__ == "__main__":
    O.report()
