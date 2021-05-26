i = 10000
passer = False
while passer != True:
    x = i
    a = 0
    b = 1
    t = 0
    while x > 0:
        if (x % 2 > 0):
            a += x % 12
        else:
            b *= x % 12
        x = x / 12
        t += 1
        if t == 128:
            x > 0
    if a == 7 and b == 12:
        print(i)
        passer = True
    i += 1