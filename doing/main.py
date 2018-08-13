# a,b=map(int, input().split())
# print(max(a,b)-min(a,b))

# arr = [0]*23

# for i in range(a):print(("%"+str(a)+"s")%("*"*(a-i)))
# a=int(input())
# print("*"*a)
# for i in range(a-2):print("*"+" "*(a-2)+"*")
# print("*"*a)

# f = open("tc.txt", "wt")
# f.write("b"*1002000)
# f.close()

# a,b=input().split()
# [print(chr(x), end=" ") for x in range(ord(a),ord(b)+1)]


user_input=input()
def f0(x):
  s = 0
  for i in range(1,len(str(x))-1):
    s += 10**(i-1)*(9*i)
  s += (10**(len(str(x))-2)*(len(str(x))-1))*(int(str(x).replace("0",""))-1)
  return s

def fn(x, n):
  s = 0
  m = int(str(x).replace("0",""))
  s = (len(str(x))-1)*10**(len(str(x))-2)*m
  if n < m:
    s += 10**(len(str(x))-1)

  return s

cnt = [0]*10
for i in range(1,int(user_input)+1):
  for j in range(10):
    cnt[j] += str(i).count(str(j))
  print(i, cnt)
print(cnt)

count = [0]*10
tmpcount = count[:]
for idx, num in enumerate(user_input):
  numint = int(num)
  
  x = numint * (10**(len(user_input) - 1 - idx))
  
  if x!=0 and x>9:
    # print(x)
    # print(f0(x), end=" ")
    count[0]+=f0(x)
    for i in range(1, 10):
      # print(fn(x, i), end=" ")
      count[i]+=fn(x,i)
    # print()
  elif len(user_input) == idx+1:
    for i in range(0, x):
      count[i]+=1

  for j in range(10):
      count[j] += str(x).count(str(j))

  for jdx, v in enumerate(tmpcount):
    count[jdx]+=v*x
    

  tmpcount[numint]+=1
  
  
  # print(tmpcount)

# if int(user_input) < 10:
count[0] -= len(user_input)-1
print(count)
# for i in inp,ut().split():
#   arr[int(i)-1]+=1
# [print(x, end=" ") for x in arr]

# input()
# print(min(list(map(int, input().split()))))

# [print(x, end=" ") for x in input().split()[::-1]]

# for i in [x for x in range(a+1) if x%3!=0]:print(i, end=" ")



# if a%7!=0:print("not",end=" ")

# print("multiple")


# a,b,c=map(int, input().split())
# m = 0
# for i in range(1, 100000000):
#   if i%b==0 and i%a==0 and i%c==0:m=i;break
# print(m)
# a,b,c,d=map(int, input().split())
# for i in range(d-1):a*=b;a+=c
# print(a)

# print(a+(c-1)*b)
# print ("%.2f MB"%((a*b*c)/(1<<23)))