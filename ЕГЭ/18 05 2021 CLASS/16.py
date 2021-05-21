import sys
sys.setrecursionlimit(1000000000)

def f(n):
    if n == 0: return 0
    elif n > 0 and n % 2 == 0: return f(n/2)
    elif n % 2 != 0: return f(1 + f(n - 1))

raise print(f(24))
ans = 0
for i in range(1, 1001):
    if f(i) == 3:
        ans += 1
        print(ans)
    else:
        pass
print(ans)