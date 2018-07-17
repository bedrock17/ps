def f(n, c):
  print("*"*c)
  if c < n:
    f(n, c+1)
    print("*"*c)
f(int(input()), 1)