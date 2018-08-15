
# print(len(input()))

# print(["lose","win"][int(float(input())//10 in [3.0, 6.0])])


# n = int(input())

# sw = 0
# for i in range(n):

#   if sw:
#     for j in range(n)[::-1]:
#       print(i*n+j+1, end=" ")
#     sw=0
#   else:
#     for j in range(n):
#       print(i*n+j+1, end=" ")
#     sw=1
    
#   print()




# def f(n):
#   if n == 1:return 1
#   return n*f(n-1)    

# a=int(input())
# print(["lose","win"][50<= a <= 70 or a%6==0])

# print(f(a))
# print(["CRASH","PASS"][int(min(list(map(int,input().split())))>170)])

# -*- coding:utf-8 -*-





# print("%.3f"%(int(input())*9/5+32))
 
# c=a-b
# d="="
# if c>0:d=">"
# elif c<0:d="<"
# print(d)
# print(int(a>=b))

# print(max(list(map(int, input().split()))))

# input()
# print(max(list(map(int, input().split()))))

# print(len([x for x in list(map(int, input().split())) if x % 2 == 0]))

# print(sum([x for x in range(a,b+1) if x%3==0]))


# l=list(map(int, input().split()))
# print("%.2f"%(sum(l)/len(l)))


# print(int(input())*24)

# print(min(list(map(int, input().split()))))
# print(a//60, a%60)

# print(input())

# print(sum([x for x in range(int(input())+1) if x%2==0]))

# if int(input())<10:print("small")
# else:print("big")

# a,b,c,d = map(int, input().split())

# a/=b
# c/=d

# if a>c:
#   print(">")
# elif a<c:
#   print("<")
# else:
#   print("=")

# l1 = list(map(int, input().split()))
# l2 = list(map(int, input().split()))


# l3 = set(l1) & set(l2)


# if l1[-1] in l3 and len(l3) == 6:
#   print("2")
# elif len(l3 - set([l1[-1]])) == 6:print("1")
# elif len(l3 - set([l1[-1]])) == 5:print("3")
# elif len(l3 - set([l1[-1]])) == 4:print("4")
# elif len(l3 - set([l1[-1]])) == 3:print("5")
# else:print("0")

# a,b=map(float, input().split())

# while a<=b:
#   print("%0.2f"%a, end=" ")
#   a+=0.01

# l = list(map(int, input().split()))
# l = list(filter(lambda x:x%5==0, l))
# if len(l)>0:
#   print(l[0])
# else:print(0)

# input()
# l=list(map(int, input().split()))
# print(l[0],l[len(l)//2],l[-1])

# a,b=map(int, input().split())
# i=a
# s=0
# while a<=b:
#   if a%2==0:
#     print("-"+str(a),end="")
#     s-=a
#   else:
#     if i==a:
#       print(str(a),end="")
#     else:
#       print("+"+str(a),end="")
#     s+=a
#   a+=1
# if s>0:
#   print("=+"+str(s))
# else:
#   print("="+str(s))


# a = int(input())
# input()
# lst = list(map(int, input().split()))

# s = a
# for i in lst:
#   s*=1+i/100


N = int(input())
count = [0]*10
tmp = count[:]
for i in range(1, N+1):
    for j in range(10):

      count[j]+=str(i).count(str(j))

    # for j in count:print(j, end=" ")
    print(i, end="====")
    for j in range(10):print(count[j]-tmp[j], end=" ")
    print()
    tmp = count[:]
print(count)

