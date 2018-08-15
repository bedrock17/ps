n = int(input())


class tree:
  def __init__(self, t):
    self.top = t
    self.left = "."
    self.right = "."
    # self.INIT = False

  def append(self, l, r):
    if l != ".":
      self.left = tree(l)

    if r != ".":
      self.right = tree(r)
  
  def find(self, value):

    # print(self.top, self.left, self.right)
    if self.top == value:
      # self.INIT = True
      return self
    
    bFind = False
    if self.left != ".":
      bFind = self.left.find(value)

    if not bFind and self.right != ".":
      bFind = self.right.find(value)

    return bFind

  def myCount(self):
    # c = 0
    # if self.INIT:
    c = 1

    if self.left != ".":
      c += self.left.myCount()
    if self.right != ".":
      c += self.right.myCount()

    return c 
  
  def printF(self):
    print(self.top, end="")
    if self.left != ".":
      self.left.printF()
    if self.right != ".":
      self.right.printF()
    
  def printM(self):    
    if self.left != ".":
      self.left.printM()
    print(self.top, end=" ")
    if self.right != ".":
      self.right.printM()
      
  def printB(self):
    if self.left != ".":
      self.left.printB()    
    if self.right != ".":
      self.right.printB()
    print(self.top, end="")

a = tree("1")

while a.myCount() < n:
  t, l, r = input().split()
  # print(t, l, r)
  nd = a.find(t)

  nd.append(l, r)

  # print(a.myCount())

# a.printF()
# print()
a.printM()
# print()
# a.printB()