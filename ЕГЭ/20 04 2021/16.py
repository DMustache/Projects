import sys
sys.setrecursionlimit(10000000)
def f(n):
    if n == 0: return print(1)
    elif n > 0 and n % 5 == 0: return print(f(n * 0.2))
    elif n > 0 and n % 5 != 0: return print(f(n % 5 * f(n * 0.2)))

lst = [float(i) for i in range(0, 21, 1)]
print(sum(lst))
for i in range(len(lst)):
    if f(lst[i]) in lst:
        lst[lst.index(f(i))] = 0