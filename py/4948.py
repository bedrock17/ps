
import math
def f(n):
  if n == 1:
    return False
  end = int(math.sqrt(n))
  for i in range(2, end+1):
    if n % i == 0:
      return False
  
  return True

while True:
  n = int(input())
  if n == 0:
    break

  count = 0
  for i in range(n+1, n*2+1):
    if f(i):
      count+=1

  print(count)
