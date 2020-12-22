coinList = [[int(j) for j in input().split()] for i in range(5)]
maxCoins0, maxCoins1, tmp = 0, 0, 0

for i in coinList[0]:
    tmp = i
    for j in coinList[1]:
        tmp += j
        for ii in coinList[2]:
            tmp +=ii
            for jj in coinList[3]:
                tmp += jj
                for iii in coinList[4]:
                    tmp += iii
                    if (tmp > maxCoins0):
                        maxCoins0 = maxCoins1
                        tmp = maxCoins0
                    tmp -= iii
                tmp -= jj
            tmp -= ii
        tmp -= j
    tmp -= i
if (maxCoins0 % 3 != 0 and maxCoins1 % 3 != 0):
    print('Save me!')
elif (maxCoins0 % 3 != 0 and maxCoins1 % 3 == 0):
    print(maxCoins0)
elif (maxCoins0 % 3 == 0 and maxCoins1 % 3 != 0):
    print(maxCoins1)
else:
    print('Save me!')