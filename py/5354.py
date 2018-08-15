m = int(input())
for j in range(m):
  n = int(input())-2
  print("#"*(n+2))
  for i in range(n):
    print("#"+"J"*n+"#")  
  if n>-1:
    print("#"*(n+2))
  if j+1 < m:
    print()