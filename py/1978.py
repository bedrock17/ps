import math
input()

count = 0
def f(n):
  global count
  
  if n == 1:
    return

  a = int(math.sqrt(n))
  for i in range(2, a+1):
    if n % i == 0:
      return
  count += 1

arr = list(map(int, input().split()))

for i in arr:
  f(i)

print(count)