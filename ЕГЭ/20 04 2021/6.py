lst = []
for N in range(10000, 1000, -1):
    nas = N
    S = 1
    while N > 0 :
        S = S * (N % 10)
        N //= 10
    if S == 12:
        lst.append(nas)
    print(S, nas)
print(lst, sum(lst))