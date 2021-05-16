lst = []
for i in range(1774, 8450):
    if int(str(sum([int(j) for j in str(i)]))[-1::]) % 2 == 0 and hex(i)[-2::] == '00':
        lst.append(i)

print(len(lst), sum(lst))