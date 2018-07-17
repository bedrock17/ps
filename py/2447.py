n = input()
a="""***
* *
***"""

def merge(a):
  out = ""
  tmp = a.replace("*", " ")
  l = a.split("\n")
  s = tmp.split("\n")

  for i in l:
    if len(i):
      out+=i*3+"\n"
  for i,v in enumerate(l):
    if len(v):
      out+= v+s[i]+v+"\n"
  for i in l:
    if len(i):
      out+=i*3+"\n"
  return out
  

def f(b):
  if b<=0:
    return "*"
  if b==1:
    return a;
  return merge(f(b/3))

print( f( int(int(n)/3) ) )