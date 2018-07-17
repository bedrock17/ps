
p = open("TC.txt", "wt")

p.write("1000 1000\n")
for i in range(1000):
  # for k in range(250):
  p.write(("1"*1+"0"*1)*500+"\n")

p.close()