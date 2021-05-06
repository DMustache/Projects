
n = 0
while int(str(n), 10) < 108:
    n += 1
    ans = n
    n = bin(n)[2::]
    if n.count('1') % 2 == 0:
        n = str(n + '00')
    else: n = str(n + '10')
print(ans)