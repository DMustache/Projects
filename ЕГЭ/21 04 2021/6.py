lst = []
for i in range(10000, 1000, -1):
    N = i
    S = 1
    while N > 0 :
        S = S * (N % 10)
        N //= 10
    if S == 6:
        lst.append(i)
print(lst)