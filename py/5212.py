"""
3 10
..........
..XXX.XXX.
XXX.......

5 5
.....
.XXX.
.....
.XXX.
.....

1 10
X........X

5 5
XXXXX
.....
XX.X.
.....
XXXXX

10 10
X.........
XX.......X
X.X.......
X..X.....X
X...X.....
X....X...X
X.....X..X
X......X.X
X.......XX
X........X

10 10
X........X
..........
....XXX...
....XXX...
.....X....
X....X...X
..........
..........
..........
.........X
"""

d = ((0, 1), (1, 0), (0, -1), (-1, 0))
n, m = map(int, input().split())
gmap = ""

def isValid(i, j):
  if 0 <= i < n:
    if 0<= j < m:
      return True 
  return False

def getChar(i, j):
  return gmap[i*m+j]

for i in range(n):
  gmap += input()

# print(gmap)
tmpmap = [c for c in gmap]
for i in range(n):
  for j in range(m):
    if getChar(i, j) == "X":
      cnt = 0
      for k, l in d:
        # print("2", k, l, isValid(i+k, j+l), getChar(i+k, j+l))
        if not isValid(i+k, j+l) or getChar(i+k, j+l) == ".":
          cnt+=1
      if cnt >=3:
        tmpmap[i*m+j] = "."


# print(tmpmap, len(tmpmap), m)
sx, sy, ex, ey = m, n, 0, 0
for i in range(n):
  for j in range(m):
    # print(tmpmap[i*m+j], end="")
    if tmpmap[i*m+j] == "X":
      if sx > j:
        sx = j
      if ex <= j:
        ex = j+1
      if sy > i:
        sy = i
      if ey <= i:
        ey = i+1
  # print()

# print(sx, sy, ex, ey)
for i in range(sy, ey):
  for j in range(sx, ex):
    print(tmpmap[i*m+j], end="")
  if i<ey-1:
    print()