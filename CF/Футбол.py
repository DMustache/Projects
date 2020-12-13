def fuc(n):
    if n == 0:
        return 1
    return fuc(n-1) * n

n = int(input())
c1 = fuc(n)//(fuc(n-11)*fuc(11))
c2 = fuc(n-11)//(fuc(n-22)*fuc(11))
print((c1*c2//2)%(1000000007))