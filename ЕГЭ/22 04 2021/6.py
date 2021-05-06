lst = []

for i in range(999, 99, -1):
    N = i
    S = 1
    while N > 0 :
        S = S * (N % 10)
        N //= 10
    if S == 6:
        lst.append(i)
for i in range(6):
    lst[i] = lst[i-1] + lst[i]
print(lst[6])