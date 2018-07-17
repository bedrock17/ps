def f(a,b):
  o = ""
  if b==1:
    o+="*"
  elif a==b:
    o+="*"*(b*2-1)
  else:
    o+="*"+" "*(b*2-3)+"*"
  
  print(" "*(a-b)+o)
  if a>b:
    f(a,b+1)

f(int(input()),1)

