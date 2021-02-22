lst = []
passer = True
tmp, tochange = 0, 0
for i in range(100):
    lst.append(int(input()))
    if 300 < lst[-1] < 1000 and lst[-1] % 7 != 0:
        for j in range(tmp, len(lst)):
            if lst[j] % 2 == 0 and passer == True:
                lst[i] = tochange
                lst[i] = lst[j]
                lst[j] = tochange
                tmp = i
                passer = False
for i in lst:
    print(i)