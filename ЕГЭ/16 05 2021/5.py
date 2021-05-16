i = 5
passer = False
num = ''
while passer == False:
    num = bin(i)[2::]
    for j in range(2):
        if num.count('1') % 2 == 0:
            num += '0'
        else:
            num += '1'
    if int(num, 2) > 103:
        print(i)
        i += 1
    else:
        i += 1
