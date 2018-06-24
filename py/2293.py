
a, b = map(int, input().split())

arr = []

for i in range(a):
  arr.append(int(input()))


count = 0

def f(n, m):
  global count
  
  if n < 0:
    return

  if n == 0:
    count += 1
    return
  
  for i in range(m, a):
    f(n - arr[i], i)
  
# print(arr)
f(b, 0)

print(count)