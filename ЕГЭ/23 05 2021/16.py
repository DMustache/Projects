import sys, math
sys.setrecursionlimit(2**23)
class test():
    #! F(0) = 0;
    #! F(n) = n + F(n – 3), если n > 0 и при этом n mod 3 = 0;
    #! F(n) = n + F(n – (n mod 3)), если n mod 3 > 0.
    def f(n):
        if n == 0:
            return 0
        elif n > 0 and n % 3 == 0:
            return n + f(n - 3)
        elif n > 1 and n % 3 > 0:
            return n + f(n - (n % 3))

def f(n):
    if n == 0:
        return 1
    elif n > 0 and n % 4 == 0:
        return f(n * 0.25)
    else:
        return n % 4 * f(math.floor(n * 0.25))
lst = [i for i in range(1, 21)]
for i in range(1, 256):
    ans = f(i)
    if ans in lst:
        lst.remove(ans)

print(sum(lst))