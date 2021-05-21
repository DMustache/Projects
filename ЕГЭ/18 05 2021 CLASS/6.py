for xx in range(2000):
    for ss in range(2000):
        s = ss
        x = xx
        s = 100*s + x
        n = 1
        while s < 2021:
            s = s + 5*n
            n = n + 1
        if n == 17:
            print(xx, ss)
            raise True
