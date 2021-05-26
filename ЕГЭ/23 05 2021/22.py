with open(r'ЕГЭ\23 05 2021\txt.txt', mode='r', encoding='utf-8') as f:
    text = f.read()
lst = []
nst = []
for i in range(len(text) - 2):
    if 'A' in text[i:i+3]:
        if text[i:i+3] not in lst:
            lst.append(text[i:i+3])
            nst.append(1)
        else:
            nst[lst.index(text[i:i+3])] += 1
print(lst[nst.index(max(nst))], max(nst))
