#int('1000', 2) 2 > 10
#(bin(9)[2::])  10 > 2

num = 0
while int(str(num), 2) < 57:
    num + 1
    num = int(str(bin(num)[2::]))
    for i in range(2):
        if str(num).count('1') % 2 == 0:
            num = int(str(num) + '1')
        else:
            num = int(str(num) + '0')
print(num, int(str(num), 2))