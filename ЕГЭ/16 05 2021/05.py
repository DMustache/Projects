ans = 0
n = 0
while ans <= 130:
    i = bin(n)[2::]
    n += 1
    if i.count('1') % 2 == 0: i += '00'
    else: i += '10'
    ans = int(i, 2)
print(ans, n - 1)
