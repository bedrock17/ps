block="""..+---+./   /|+---+ ||   | +|   |/.+---+..""" #블록
def draw(c,z,x,y): #그리는 함수
  cy=height-4-y*3+z*2-len(arr)*2
  cx=(h-z-1)*2+x*4
  for i in range(6):
    for j in range(7):
      ch=block[i*7+j]
      if ch!='.':
        c[cy+i][cx+j]=ch
h,w=map(int,input().split())  #가로 세로
arr=[]
for i in range(h):
  arr.append(list(map(int,input().split())))
height=0
for i,row in enumerate(arr):
  for j,v in enumerate(row):
   height=max(height,v*3+(len(arr)-i)*2+1)  #최대 높이
canvas=[['.']*(w*4+h*2+1)for x in range(height)]
for i in range(h):
  for j in range(w):
    for k in range(arr[i][j]):
      draw(canvas,i,j,k)
out =""
for i in canvas:
  for j in i:
    out+=j
  out+="\n"
print(out)