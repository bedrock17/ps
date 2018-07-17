n, m = map(int, input().split())

myqueue = []
arr = []
for i in range(n):
  arr.append([])
  arr[i]= [int(x) for x in input()]

item = {"i": 0, "j": 0, "count": 1}
myqueue.append(item)
while len(myqueue) != 0:
  now = myqueue[0]
  myqueue=myqueue[1:]

  if arr[now["i"]][now["j"]] == 0:
    continue
  arr[now["i"]][now["j"]] = 0 
  # print(now)
  if now["i"] +1 == n and now["j"] +1 == m:
    print(now["count"])
    break
  if now["i"] + 1 < n:
    if arr[now["i"]+1][now["j"]] == 1:
      myqueue.append({"i": now["i"]+1, "j": now["j"], "count":now["count"]+1})

  if now["i"] - 1 >= 0:
    if arr[now["i"]-1][now["j"]] == 1:
      myqueue.append({"i": now["i"]-1, "j": now["j"], "count":now["count"]+1})

  if now["j"] + 1 < m:
    if arr[now["i"]][now["j"]+1] == 1:
      myqueue.append({"i": now["i"], "j": now["j"]+1, "count":now["count"]+1})

  if now["j"] - 1 >= 0:
    if arr[now["i"]][now["j"]-1] == 1:
      myqueue.append({"i": now["i"], "j": now["j"]-1, "count":now["count"]+1})
