f = open(f'ЕГЭ\\07 05 2021\\file.txt', encoding='utf-8', mode='r')
tt = f.read()
f.close
lst = []
mst = []
for i in range(len(tt)-2):
    tr = tt[i] + tt[i + 1] + tt[i + 2]
    if 'A' in tr and tr not in lst:
        lst.append(tr)
        mst.append(1)
    elif 'A' in tr and tr in lst:
        mst[lst.index(tr)] += 1
    else:
        continue
print(tr, '\n', max(mst), lst[mst.index(max(mst))], mst.count(max(mst)))