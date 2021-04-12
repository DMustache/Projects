def f(n):
    if n == 0:
        return 0
        if n % 2 ==0:
            return f(n // 2)
        return 1 +f(n-1)
inp = n-1
while f(inp) != 11:
    inp +=1
print(inp)

for inp in range(1000000):
    if f(inp) == 11:
        print(inp)
        break