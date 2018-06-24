import math


q = input().split()
a = int(q[0]); b = int(q[1])

def f(n):
  if n == 1:
    return False
  end = int(math.sqrt(n))
  for i in range(2, end+1):
    if n % i == 0:
      return False
  
  return True



for i in range(a, b+1):

  if f(i):
    print(i)