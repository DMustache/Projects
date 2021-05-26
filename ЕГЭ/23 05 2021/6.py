lst = []
i = 1000
while len(lst) != 6:
    N = i
    S = 1
    while N > 0 :
        S = S * (N % 10)
        N //= 10
    if S == 6:
        lst.append(i)
    i += 1
print(lst, sum(lst), len(lst), max(lst))