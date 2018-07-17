def f(n):
  if n<9:
    return n%9;
  return f(int(n/9))*10 + n%9
print(f(int(input())))
