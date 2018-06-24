N = int(input())
count = 0
if N > 0:
  N -= 1
  count += 1
while N > 0:
  N -= count * 6
  count += 1
print(count)