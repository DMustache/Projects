def nnn(n, de):
    if n % de == 0:
        return n // de
    else:
        return n - 1

ans = 0
for n in range(10000):
    lst = [2, 3, 7]
    for i in lst:
        n = nnn(n, i)
    if n == 1:
        ans += 1
print(ans)