lst, i, = [], 100
while len(lst) != 5:
    N = i
    S = 1
    while N > 0 :
        S = S * (N % 10)
        N //= 10
    if S == 12:
        lst.append(i)
    i += 1
print(sum(lst), *lst)