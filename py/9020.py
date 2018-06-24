import math
def f(n):
  if n == 1:
    return False
  end = int(math.sqrt(n))
  for i in range(2, end+1):
    if n % i == 0:
      return False
  
  return True

n = int(input())
arr = []
for i in range(n):
  arr.append(int(input()))

for i in arr:
  for j in range(int(i/2)):
    j = int(i/2 - j)
    if f(j):
      if f(i-j):
        print(j, i-j)
        break