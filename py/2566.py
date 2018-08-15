m=0
for i in range(9):
  l=list(map(int,input().split()));c=max(l)
  if c>m:m=c;a=i+1;b=l.index(c)+1
p=print;p(m);p(a,b)