
f = open("calc.txt", "wt")
for i in range(101):
  for j in range(101):
    f.write("7 9 10 " + str(i) + " " + str(j) + "\n")
f.close()


# f = open("calc.txt", "rt")

# txt = f.read(100 << 10)
# lines = txt.split('\n')

# f.close()
# f = open("calc.txt", "wt")
# for i in lines:
#   if "!" in i:
#     f.write(i+"\n")

# f.close()