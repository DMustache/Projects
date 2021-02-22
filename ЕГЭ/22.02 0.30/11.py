def F(n):
  if n > 2:
    print(n,end='')
    F(n-1)
    G(n-2)
  else:
    print(n+2,end='')
def G(n):
  print(n,end='')
  if n > 2:
    F(n-2)
    G(n-1)
  else:
    print(n+1,end='')
F(5)