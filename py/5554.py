a=[]
exec("a.append(int(input()));"*10)
print(a[0]-sum(a[1:]))