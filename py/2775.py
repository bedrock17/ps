
mymap = [[-1] * 15 for i in range(15)]

def f(a, b):
  if a == 1:
    return int(((b+1)*b)/2)
  elif a == 0:
    return b
  
  s = -1
  if mymap[a][b] == -1:
    s = sum([f(a-1, x+1) for x in range(b)])
    mymap[a][b] = s
  else:
    s = mymap[a][b]

  return s

N = int(input())
for i in range(N):
  a = int(input())
  b = int(input())
  print(f(a, b))
