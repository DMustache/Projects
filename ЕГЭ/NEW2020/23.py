n, bank = 500, 4000000
Alst = []
Acur = []
Blst = []
Bcur = []

f = open(r'ЕГЭ\NEW2020\05.txt', mode='r')
for i in f:
    tmp = 0
    for j in range(len(i)):
        ct, cur, market = '','',''
        if i[j] == ' ':
            tmp += 1
        else:
            if tmp == 0:
                ct += i[j]
            elif tmp == 1:
                cur += i[j]
            else:
                market = i[j]
                break
    int(ct), int(cur), str(market)
    if market == 'A':
        Alst.append(ct)
        Acur.append(cur)
    elif market == 'B':
        Blst.append(ct)
        Bcur.append(cur)
    else:
        continue
del ct, cur, market

buycan = False
while buycan != True:
    for i in range(len(Alst)):
        