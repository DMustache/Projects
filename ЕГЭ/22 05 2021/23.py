for i in range(536792, 604299):
    k = 0
    d = 2
    a = []
    while d * d < i:
        if i % d == 0:
            k += 2
            a.append(d)
            a.append(i // d)
        d += 1
    if k == 3:
        print(*a)