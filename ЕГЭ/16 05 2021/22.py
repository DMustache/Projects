with open(r'ЕГЭ\16 05 2021\file.txt', mode='r', encoding='utf-8') as f:
    text = f.read()

lst = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
abc = ''.join(lst)

elems = []
for i in range(len(text) - 1):
    passer = False
    elems.append(text[i])
    j = 1
    while passer == False:
        if len(text) < i + j + 1:
            passer = True
        else:
            if ord(text[i + j]) == ord(elems[-1][-1]) or ord(text[i + j]) + 1 == ord(elems[-1][-1]):
                elems[-1] += text[i + j]
            else:
                passer = True
        j += 1
print(max(elems, key=len))