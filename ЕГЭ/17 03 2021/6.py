ans = 0
s = 5
n = 0
while n != 11:
    n += 1
    s += 1
    s = s * 10 - 5
    while s < 2021:
        s += 2 * n
        n += 1
    print(s)