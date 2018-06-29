


a = int(input())
c = 1
while a > c * 10:
  a+=c*5
  c*=10
  a-=a%c
print(a)
  