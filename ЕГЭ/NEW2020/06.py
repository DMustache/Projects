f = open(r"ЕГЭ\NEW2020\05.txt", mode='r')
txt = f.read()
f.close()
lst = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
numlst = [0 for i in range(len(lst))]
for i in range(1, len(txt) - 1, 1):
    if txt[i - 1] == txt[i + 1]:
        numlst[lst.index(txt[i])] += 1

print(lst[numlst.index(max(numlst))])