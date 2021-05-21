
n = 3
a = 0
while a != 20:
    ct = 0
    n+= 1
    x = n
    a = 3*x+23
    b = 3*x-17
    while a != b:
        if a>b:
            a-=b
        else:
            b-=a
        if ct == 200:
            a = 200
            b = 200
        ct += 1
print(n)
