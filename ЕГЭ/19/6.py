lst = [i for i in range(1000, 10000)]
ans = []
for N in lst:
    S = 1
    n = N
    while N > 0:
        S = S * (N % 10)
        N = N // 10
    if S == 9:
        print(n)
        ans.append(n)
for i in range(len(ans) - 5, len(ans), -1):
    print(ans[i])
print(ans[-1::-5])
print(sum(ans[-1::-5]))