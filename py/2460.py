tot,ma=0,0
while True:
  n,m = map(int,input().split())
  tot+=(m-n)
  if tot>ma:ma=tot
  if tot<=0:break
print(ma)
  