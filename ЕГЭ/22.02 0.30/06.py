
def filter(num):
    tmp0 = int(str(num)[0])
    tmp1 = int(str(num)[1])
    tmp2 = int(str(num)[2])
    tmp3 = int(str(num)[3])

    tmp0 = tmp0 + tmp1
    tmp1 = tmp1 + tmp2
    tmp2 = tmp2 + tmp3
    if min(tmp0, tmp1, tmp2) == tmp0:
        if tmp1 < tmp2:
            return f'{tmp2}{tmp1}'
        else:
            return f'{tmp1}{tmp2}'

    elif min(tmp0, tmp1, tmp2) == tmp1:
        if tmp0 < tmp2:
            return f'{tmp2}{tmp0}'
        else:
            return f'{tmp0}{tmp2}'

    elif min(tmp0, tmp1, tmp2) == tmp2:
        if tmp0 < tmp1:
            return f'{tmp1}{tmp0}'
        else:
            return f'{tmp0}{tmp1}'
f = open(r'ЕГЭ\22.02 0.30\txt.txt', mode='w')
for i in range(1000, 10000):
    changed = filter(i)
    f.write(f'{i}, {changed}\n')
    if changed == 1414:
        print(changed, i)
f.close()