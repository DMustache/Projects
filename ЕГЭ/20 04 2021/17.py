#int('1000', 8) # 8 > 10
#(bin(9)[2::])  # 10 > 2
#sum([int(str(1234)[i]) for i in range(len(str(1234)))]) #сумма цифр числа
lst = []
for j in range(1686, 6974):
    if sum([int(str(j)[i]) for i in range(len(str(j)))]) % 3 == 0 and str(int(bin(j)[2::], 8))[::1] == '33':
        lst.append(j)
print(len(lst), sum(lst))