lst = []
for i in range(25317, 51238):
    ans = 0
    passer = True
    for j in range(i // 2 + 1, 1, -1):
        if i % j == 0:
            if passer == True:
                mx, passer = j, False
            ans += 1
            if ans == 6:
                lst.append(f'{i} {mx} \n')
                break
with open(r'ЕГЭ\23 05 2021\fle.txt', mode='w', encoding='utf-8') as f:
    for i in range(len(lst)):
        f.writelines(lst[i])