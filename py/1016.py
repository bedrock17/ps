import math 

a, b = map(int, input().split())

_max = int(math.sqrt(b) + 1)
# _min = int(math.sqrt(a) - 1)

queue = [x for x in range(2, _max)]

count = 0

mydic = {}


if len(queue) != 0:
  i = queue[0]
  queue = queue[1:]
else:
  i = 2

check = i ** 2
while (check <= b):
  
  j = check
  jcount = 1
  
  # print(i)
  while j <= b:
    if a <= j and not(j in mydic and mydic[j]):
      # print(j)
      mydic[j] = True
      count += 1

    if j < a:
      jcount = int(a/check) + 1
    else:
      jcount += 1

    j = check * jcount

  if (check < math.sqrt(queue[-1])):
    queue = [x for x in queue if x % i != 0]
  # print(i)
  # print(queue)

  print(i, len(queue), count)

  if len(queue) == 0:
    break  
  i = queue[0]
  queue = queue[1:]

  check = i**2

print((b - a +1 ) - count)