with open(r'ЕГЭ\18 05 2021 CLASS\file.txt', mode='r', encoding='utf-8') as f:
    text = f.readlines()
lst = []
for i in range(len(text)):
    if text[i].count('G') > 25:
        string = text[i]
        mlst = []
        for s in range(0, len(string) - 2, 1):
            for e in range(len(string) -1, s, -1):
                if string[s] == string[e]:
                    mlst.append(e - s)
        lst.append(max(mlst))
print(lst)
print(max(lst))
