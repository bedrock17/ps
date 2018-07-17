a,b=map(int,input().split())
arr=[]
k = {}
for i in range(a):
  arr.append(int(input()))
arr=arr[::-1]

m = -1
def f(n):
  global m
  if n==0:
    return 1;
  c = -1
  for i in arr:
    if n-i in k:
      return k[n-i]
    

f(b)
print(m)

#씨발 아직 못풀었으니 나중에 이거보면 풀자