
# import time
# start_time = time.time()

# n,m=map(int,input().split())

# arr = []
# for i in range(n):
#   arr.append(input())
# start_time = time.time() 
# maxsz = 0


# def getSize(_i, _j):
  
#   check_len = min(n - _i, m - _j)
#   if check_len <= maxsz:
#     return 0
#   if check_len == 1:
#     return 1
  
#   # print("dbg : ", _i, _j, check_len, maxsz)
#   if maxsz:
#     if arr[_i][_j:_j+maxsz+1] != "1"*(maxsz+1):
#       return -1

#   count = 0
  
#   for i in range(0, check_len):
#     i+=1
#     for j in range(0, i):
#       # print("!", _i, j, _j, i , arr[_i+j][_j:_j+i], "1"*(i), count)
#       if arr[_i+j][_j:_j+i] != "1"*(i):

#         return count
#     count+=1

#   return count

# for i, iv in enumerate(arr):
#   if n - i > maxsz:
#     for j, jv in enumerate(iv):
#       if m - j > maxsz:
#         if jv == "1": 
#           tmp = getSize(i, j)
#           # print("========>", i, j, tmp)
#           if tmp > maxsz:
#             # print(i, j)
#             maxsz = tmp
# print(maxsz**2)
# print("--- %s seconds ---" %(time.time() - start_time))



n,m=map(int,input().split())

arr = []
for i in range(n):
  arr.append(input())

maxsz = 0

def getSize(_i, _j):
  
  check_len = min(n - _i, m - _j)
  if check_len <= maxsz:
    return 0
  if check_len == 1:
    return 1

  if maxsz:
    if arr[_i][_j:_j+maxsz+1] != "1"*(maxsz+1):
      return -1

  count = 0
  
  for i in range(0, check_len):
    i+=1
    for j in range(0, i):
      if arr[_i+j][_j:_j+i] != "1"*(i):

        return count
    count+=1

  return count

for i, iv in enumerate(arr):
  if n - i > maxsz:
    for j, jv in enumerate(iv):
      if m - j > maxsz:
        if jv == "1": 
          tmp = getSize(i, j)
          if tmp > maxsz:
            maxsz = tmp
print(maxsz**2)