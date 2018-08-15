f = open("calc.txt", "rt")

txt = f.read(100 << 10)
lines = txt.split('\n')

f.close()
f = open("calc.txt", "wt")
for i in lines:
  if "!" in i:
    f.write(i+"\n")

f.close()