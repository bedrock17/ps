
n = int(input())
a = []
for i in range(n):
  a.append(int(input()))


b = []
st = []
out = []

i = 1
focus = 0

if n == 1:
  print("+")
  print("-")

while i <= n + 1:
  if i <= n:
    if len(st) == 0 or st[-1] != a[focus]: 
      st.append(i)
      out.append("+")
      i+=1

  if len(st) == 0:
    break
  

  
  if st[-1] == a[focus]:
    out.append("-")
    b.append(st.pop())
    focus+=1
  elif a[focus] in st:
    break

if a != b:
  print("NO")
else:
  for i in out:
    print(i)


