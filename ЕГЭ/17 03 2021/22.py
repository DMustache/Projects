f = open(r'ЕГЭ\17 03 2021\file.txt', encoding='utf-8', mode='r')
lst = []
txt = f.readlines()
f.close()
for i in txt:
    lst.append(i.count('N'))

minstr = txt[lst.index(min(lst))]
abc = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
ins = [0 for i in range(len(abc))]

for i in minstr[:-1]:
        ins[abc.index(i)] += 1

if ins.count(max(ins)) != 1:
    abc.reverse()
    ins.reverse()
    print(abc[ins.index(max(ins))])
else:
    print(abc[ins.index(max(ins))])