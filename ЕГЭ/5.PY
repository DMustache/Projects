i = 0
ans = '00'
while int(ans, 2) <= 96:
    i += 1
    ans = bin(i)[2::]
    if sum([int(j) for j in str(ans)]) % 2 == 0:
        ans += '00'
    else:
        ans += '10'
print(ans, int(ans, 2), i)