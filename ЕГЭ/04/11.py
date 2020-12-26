def F(n):
    if n > 0:
        print(n,end='')
        G(n-2)
        F(n-1)
    else:
        print(n+2,end='')
def G(n):
    print(n,end='')
    if n > 2:
        F(n-2)
        G(n-1)
print(F(6))