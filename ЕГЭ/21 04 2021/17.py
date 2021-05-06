def to7(n):
    ans = ''
    while n > 0:
        ans = str(n % 7) + ans
        n = n // 7
    return ans

lst = []
for i in range(1343, 7946):
    if sum([int(j) for j in str(i)]) and to7(i)[:3:] == '420':
        lst.append(i)
print(len(lst), lst[-1], lst)