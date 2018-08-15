"""
1
5
50 10 100 20 40
30 50  70 10 60
"""
import sys
dp = [ [0 for x in range(100005)], [0 for x in range(100005)] ]
sys.setrecursionlimit(100005)

def f(i, j):
  if j >= n-1:
    return arr[i][n-1]
  nxti = 0
  if i == 0:
    nxti = 1
  if dp[i][j]==0:
    dp[i][j] = max(f(nxti, j+1), f(nxti, j+2)) + arr[i][j]
  return dp[i][j]

a = int(input())
for i in range(a):
  n = int(input())
  arr = []
  for j in range(n):
    dp[0][j] = 0
    dp[1][j] = 0
  arr.append(list(map(int, sys.stdin.readline().split())))
  arr.append(list(map(int, sys.stdin.readline().split())))

  print(max(f(0, 0), f(1, 0)))

