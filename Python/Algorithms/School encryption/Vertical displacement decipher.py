def quick_sort(data):
    def sort(s_data, fst, lst):
        if fst >= lst:
            return

        i, j = fst, lst
        x = s_data[(fst + lst) // 2]

        while i <= j:
            while s_data[i] < x:
                i += 1
            while s_data[j] > x:
                j -= 1
            if i <= j:
                s_data[i], s_data[j] = s_data[j], s_data[i]
                i, j = i + 1, j - 1
            sort(s_data, fst, j)
            sort(s_data, i, lst)

        return s_data

    return sort(list(data), 0, len(data) - 1)

key = 'ДЯДИНА'
chipher = 'ОЯЕ АВ ЕРИЕИАЛРЧМЬГ Б СВ'
HZSkolkoGrammi = [[' ' for i in range(4)] for j in range(6)]

tmp = 0
for i in range(6):
    for j in range(4):
        try:
            HZSkolkoGrammi[i][j] = chipher[tmp]
            tmp += 1
        except IndexError:
            continue
    print(HZSkolkoGrammi[i])

keySorted = quick_sort(key)
indexList = []
for i in range(len(key)):
    indexList.append(keySorted.index(key[i]))
print(indexList)

answer = ''
for i in range(len(key)):
    while indexList.count(i) != 0:
        for j in indexList:
            answer += HZSkolkoGrammi[i][min(indexList)]
            indexList[indexList.index(j)] = 255
print(answer)