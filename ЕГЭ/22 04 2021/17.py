def to6(n):
    ans = ''
    while n > 6:
        ans = str(n % 6) + ans
        n = n // 6
    return str(n) + ans

lst = []
for i in range(1128, 9736):
    if sum([int(j) for j in str(i)]) % 2 == 0 and to6(i)[1::]:
        lst.append(i)
print(len(lst), max(lst))