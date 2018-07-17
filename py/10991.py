def f(a,b):
  o = ""
  if b==1:
    o+="*"
  else:
    for i in range(b*2):
      if i%2==0:
        o+="*"
      else:
        o+=" "
  print(" "*(a-b)+o)
  if a>b:
    f(a,b+1)

f(int(input()),1)

