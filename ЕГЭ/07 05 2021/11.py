ans = ''
tmp = 0
while ans != '7 12':
    tmp += 1
    int(x) = tmp
    int(a) = 0
    int(b) = 1
    while x > 0:
        if (x % 2 > 0):
            int(a) += x % 12
        else:
            int(b) *= x % 12
        x = x / 12
    print(a, b, tmp)
    ans = f'{a} {b}'

print(tmp)