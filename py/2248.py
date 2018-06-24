N = int(input())
out = """  *  
 * * 
*****"""
def merge(s):
  arr = s.split('\n')
  out = ""
  for i in range(len(arr)):
    out += " " * (len(arr)) + arr[i] + " " * (len(arr)) + '\n'

  for i in range(len(arr)):
    out += arr[i] + " " + arr[i]
    if i < len(arr) - 1:
      out += '\n'
  
  return out

def f(o, N):
  if N == 1:
    return o
  else:
    o = merge(o)
    return f(o, N/2)

N = int(N/3)
print(f(out, N))