import math
import itertools

class union_find:
  def __init__(self, n):
    self.parent = [-1] * n
    self.size = [1] * n

  def root(self, x):
    if self.parent[x] == -1:
      return x
    else:
      self.parent[x] = self.root(self.parent[x])
      return self.parent[x]

  def is_same(self, x, y):
    return self.root(x) == self.root(y)

  def unite(self, x, y):
    x = self.root(x)
    y = self.root(y)

    if x == y:
      return False

    else:
      if self.size[x] < self.size[y]:
        x, y = y, x

      self.parent[y] = x;
      self.size[x] += self.size[y]
      return True

  def get_size(self, x):
    return self.size[self.root(x)]


h, w = map(int, input().split())
q = int(input())
uf = union_find(h * w + 1)
m = [-1] * (h * w + 1)

def check(n, x):
  if m[x] == 1 and m[n] == 1:
    uf.unite(n, x)
  return

for i in range(q):
  a = list(map(int, input().split()))

  if a[0] == 1:
    n = w * (a[1] - 1) + (a[2] - 1)
    m[n] = 1

    if n - w >= 0:
      check(n, n - w)
    if n + w < h * w:
      check(n, n + w)
    if n % w != 0 and n - 1 >= 0:
      check(n, n - 1)
    if (n + 1) % w != 0 and n + 1 < h * w:
      check(n, n + 1)
  else:
    n1 = w * (a[1] - 1) + (a[2] - 1)
    n2 = w * (a[3] - 1) + (a[4] - 1)

    if uf.is_same(n1, n2) and m[n1] == 1 and m[n2] == 1:
      print("Yes")
    else:
      print("No")
