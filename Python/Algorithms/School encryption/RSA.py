noToUse = []
def delimiter():
    global lst, noToUse
    i = 0
    for i in range(len(lst)):
        if lst[i] != 0 and lst[i] not in noToUse:
            noToUse.append(lst[i])
            return lst[i]
n = 100
lst = [i for i in range(2, n + 1)]
print(*lst)
print(delimiter())
sqrt = int(round(n**0.25) + 1)
print(sqrt)
for i in range(sqrt):
    tmp = delimiter()
    for j in range(2, len(lst)):
        if lst[j] % tmp == 0:
            lst[j] = 0
print(*lst)