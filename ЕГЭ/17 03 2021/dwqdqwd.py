x = int(input())
k = x % 9
a = 0
b = 0
while x > 0:
    d = x % 9
    if d == k:
        a += 1
    b += d
    x //= 9
print(a, b)