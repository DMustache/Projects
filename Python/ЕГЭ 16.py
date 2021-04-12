def step(num):
    if num == 0:
        return 0
    if num % 2 == 0:
        return step(num //2)
    return 1 + step(num - 1)

tmp = 0
while step(tmp) != 11:
    tmp += 1
print()