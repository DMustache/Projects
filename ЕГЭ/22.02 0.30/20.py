x, a, b = 0, 0, 0
f = open(r'ЕГЭ\22.02 0.30\txt.txt', 'w')
for i in range(9999999):
    x = i
    a= 0
    b =1
    while x > 0:
        a += 1
        if x % 14 != 0:
            b *= x % 14
        x = x / 14
        if x < 1:
            x = 0
    f.write(f'{a} {b}\n')
f.close()