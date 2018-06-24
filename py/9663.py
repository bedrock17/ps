N = int(input())
count = 0

def f(m, i):
  global count

  for j in range(N):

    if m[i][j] == 0:
      if i == N - 1:
        count += 1
        # return
        # print("===================", i, j)
        # for l in m:
        #   print(l)
        return

      tm = []
      for r in range(N):
        tm.append([])
        for c in range(N):
          tm[r].append(m[r][c])
      tm[i][j] = 1
      
      for k in range(1, N):

        if i + k < N:
          tm[i + k][j] = 2
        
          if j + k < N:
            tm[i + k][j + k] = 2
          if j - k >= 0:
            tm[i + k][j - k] = 2
        else:
          break
      # print("!!")
      # print(m)
      # print(tm)
      # print("!!")

      f(tm, i + 1)

m = [[0] * N for i in range(N)]

f(m, 0)

print(count)