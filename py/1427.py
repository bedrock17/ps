a = [int(x) for x in input()]
a.sort(reverse=True)
b = ""
for i in a: b+= str(i)
print(b)