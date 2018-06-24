
for i in range(int(input())):
 a, b, c = map(int, input().split())
 c -= 1
 print("%d%02d"%((c)%(a)+1, int(c/a)+1))
 