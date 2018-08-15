n, m, q = map(int, input().split())

org = input()[:n]
sub = input()[:m]
# print(org)
# print(sub)
for i in range(q):
  a, b = map(int, input().split())
  cnt = 0
  if b - a + 1 >= m:
    # print(a-1, b - m)
    for i in range(a-1, b - m + 1):
      
      if org[i:i+m] == sub:
        cnt += 1
  print(cnt)