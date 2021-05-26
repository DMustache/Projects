i = 1
while True:
    x, a, b = i, 0, 1
    tp = 0
    while x > 0:
        a += 1
        if x % 12 != 0:
            b = b * (x % 12)
        x = x // 12
        if tp == 256:
            x, a, b = 0, 0, 0
    if a == 2 and b == 10:
        print(i, a, b)
    i += 1