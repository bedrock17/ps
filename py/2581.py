
a = int(input())
b = int(input())

import math
def f(n):
  if n == 1:
    return False
  end = int(math.sqrt(n))
  for i in range(2, end+1):
    if n % i == 0:
      return False
  
  return True

min = -1
count = 0

for i in range(a, b+1):

  if f(i):
    if min == -1:
      min = i
    count += i

if count != 0:
  print(count)
print(min)