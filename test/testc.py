def find(a):
  for i in range(0, 9):
    for j in range(0, 9):
      if a[i][j] == 0:
        return i, j
  return -1, -1

count = 0
import time
def printf(arr, dep):
  global count
  count+=1
  if count % 1 != 0:
    return
  for i in arr:
    for j in i:
      print(str(j) + " ", end="")
    print()
  print("===========", dep, count)
  time.sleep(0.1)

def check(arr, i, j):
  n = 0 #0b000000000
  for k in range(9):
    if arr[i][k] != 0:
      n |= 1 << (arr[i][k]-1)
    if arr[k][j] != 0:
      n |= 1 << (arr[k][j]-1)
    
  l, m = int(i/3)*3, int(j/3)*3

  for u in range(3):
    for y in range(3):
      if arr[l+u][m+y] != 0:
        n |= 1 << (arr[l+u][m+y]-1)

  return n 

def step(arr):
  lst = []
  bAble = True
  for i in range(9):
    for j in range(9):
      if arr[i][j] == 0:
        n = check(arr, i, j)
        c = 0
        idx = -1
        for k in range(9):
          if not(n & (1 << k)):
            c+=1
            idx = k
        if c == 1:
          lst.append((i,j))
          arr[i][j] = idx + 1
        elif c == 0:
          bAble = False

  return lst, bAble


def f(a, i, j):
  # printf(a, "%02d"%(i*10+j))
  i, j = find(a);
  if i == -1:
    return True

  n = check(arr, i, j)
  for k in range(0, 9):
    if not(n & (1 << k)):
      a[i][j] = k + 1
      lst, b = step(a)
      
      if b:
        if f(a, i, j):
          return True
      a[i][j] = 0  
      for s in lst:
        a[s[0]][s[1]] = 0    
    

  return False


arr = []

for i in range(9):
  arr.append([])
  for j in list(map(int,input().split())):
    arr[i].append(j)


end = f(arr, 0, 0)

if end:
  for i in arr:
    for j in i:
      print(str(j) + " ", end="")
    print()
else:
  print("NO ANS")