
opers = ["+", "-", "/", "*"]
bFind = False
def find2(opers, ns, val):
  global bFind
  a, b, c = opers
  for i, v in enumerate(ns):
    ns1 = ns[:]
    if not bFind:
      del ns1[i]
      for i2, v2 in enumerate(ns1):
        ns2 = ns1[:]
        del ns2[i2]
        if not bFind:
          for i3, v3 in enumerate(ns2):
            ns3 = ns2[:]
            del ns3[i3]
            if not bFind:
              for i4, v4 in enumerate(ns3):       
                try:
                  value = eval(v + a + v2 + b + v3 + c + v4)
                  if abs(value - val) < 0.00001: bFind = True
                except:pass                
                try:
                  value = eval(v + a + v2 + b + "(" + v3 + c + v4 + ")")
                  if abs(value - val) < 0.00001: bFind = True
                except:pass
                try:
                  value = eval("("+v + a + v2 + ")" + b + v3 + c + v4)
                  if abs(value - val) < 0.00001: bFind = True
                except:pass
                try:
                  value = eval("("+v + a + v2 + ")" + b + "(" + v3 + c + v4 + ")")
                  if abs(value - val) < 0.00001: bFind = True
                except:pass
                try:
                  value = eval(v + a + "("+ v2 + b + v3 + ")" + c + v4)
                  if abs(value - val) < 0.00001: bFind = True
                except:pass
                try:
                  value = eval("(("+v + a + v2 + ")" + b + v3 + ")"+ c + v4)
                  if abs(value - val) < 0.00001: bFind = True
                except:pass
                try:
                  value = eval("("+v + a + v2 + b + v3 + ")" + c + v4)
                  if abs(value - val) < 0.00001: bFind = True
                except:pass
                try:
                  value = eval("("+v + a + "(" + v2 + b + v3 + "))" + c + v4)
                  if abs(value - val) < 0.00001: bFind = True
                except:pass
                try:
                  value = eval(v + a + "(" + v2 + b + "(" + v3 + c + v4 + "))")
                  if abs(value - val) < 0.00001: bFind = True
                except:pass
                try:
                  value = eval(v + a + "(" + v2 + b  + v3 + c + v4 + ")")
                  if abs(value - val) < 0.00001: bFind = True
                except:pass
                try:
                  value = eval(v + a + "((" + v2 + b  + v3 + ")" + c + v4 + ")")
                  if abs(value - val) < 0.00001: bFind = True
                except:pass

                # if bFind:
                #   print(v, a, v2, b, v3, c, v4)

gCon = True
def find():
  global bFind
  global gCon
  inp = input()
  if inp == "-1":
    gCon = False
    return
  bFind = False
  inp1 = inp.split()
  ns = inp1[:]
  val = 24
  
  for i in opers: 
    if not bFind:
      for j in opers:
        if not bFind:
          for k in opers:
            if not bFind:
              find2([i, j, k], ns, val)
  
  if bFind:
    print("YES")
  else:
    print("NO")


count = int(input())
while count > 0:
  find()  
  count-=1