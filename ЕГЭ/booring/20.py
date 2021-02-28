s, a, b = 0, 0, 0
ans = 0
for x in range(999):
    a = 0
    b = 1
    while x > 0:
        a += 1
        if x % 12 != 0:
            b *= x % 12
        x = x / 12
    print(a, b)
    if a == 2 and b == 10:
        ans += 1
print(ans)