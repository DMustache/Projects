f = open(r'ЕГЭ\17 03 2021\file.txt', encoding='utf-8', mode='w')
for i in range(1000):
    x = i
    k = x % 9
    a = 0
    b = 0
    while x > 0:
        d = x % 9
        if d == k:
            a += 1
        b += d
        x //= 9
    f.write(f'{a} {b} {i}\n')