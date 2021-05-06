f = open(f'ЕГЭ\\22 04 2021\\file.txt', mode='r', encoding='utf-8')
txt = f.read()
f.close()
trg = []
ctg = []
tg = ''
for i in range(len(txt) - 3):
    tg = str(txt[i] + txt[i + 1] + txt[i + 2])
    if tg not in trg:
        trg.append(tg)
        ctg.append(1)
    else:
        ctg[trg.index(tg)] += 1
print(trg, trg[ctg.index(max(ctg))])
print(ctg, ctg.count(max(ctg)), max(ctg))