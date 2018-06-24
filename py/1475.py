
n = input()

arr = [0] * 9

for i in n:
  a = int(i)
  if a == 9:
    a = 6
  
  arr[a] += 1

arr[6] = arr[6] / 2

if (arr[6] != int(arr[6])):
  arr[6] += 1

arr[6] = int(arr[6])

count = max(arr)

print(count)
