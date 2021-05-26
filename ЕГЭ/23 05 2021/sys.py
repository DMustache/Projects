string = '9AAAAAAAA5000000005AAAAAAA900000A0000000000'
lst = []
for i in string:
    if i == 'A':
        lst.append(11)
    else:
        lst.append(int(i))
print(lst, sum(lst))
 