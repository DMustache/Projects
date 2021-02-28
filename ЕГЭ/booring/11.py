def F(n):
  if n > 0:
    print("B",end='')
    G(n-1)
def G(n):
  if n > 1:
    print("A",end='')
    F(n-2)
a = F(13)

print(a)