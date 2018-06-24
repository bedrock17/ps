
def f(n, m, count):
  
  ret_end = False
  ret_count = -1
  
  if n == 0 and m == 1:
    return True, count

  if n < 0 or m < 0:
    return False, count

  for i in range(-1, 2):
    if m + i < 1:
      continue
    end, ch_count = f(n - (m+i), m + i, count + 1)
    if end == True:
      if ret_count == -1 or ch_count < ret_count:
        ret_end = end
        ret_count = ch_count
  
  return ret_end, ret_count


def ff(n):
  c = 1
  count = 0

  while (n > 0):
    n -= c
    count += 1
    if count % 2 == 0:
      c += 1

  return count

  
N = int(input())

def f(l):
  return abs(l[0] - l[1])
for i in range(N):
  a = f(list(map(int, input().split())))

  print(ff(a))