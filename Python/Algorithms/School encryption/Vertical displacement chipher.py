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
letter = 'АБРАМОВ ИЛЬЯ СЕРГЕЕВИЧ'
abcMap = [[' ' for i in range(len(key))] for j in range(len(letter) // len(key) + 1)]
tmp = 0
for i in range(len(abcMap)):
    for j in range(len(key)):
        try:
            abcMap[i][j] = letter[tmp]
            tmp += 1
        except IndexError:
            continue
    print(abcMap[i])

keySorted = quick_sort(key)
indexList = []
abc = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
for i in range(len(key)):
    indexList.append(keySorted.index(key[i]))

answer = ''
for i in range(len(key)):
    while indexList.count(i) != 0:
        for j in range(len(letter) // len(key) + 1):
            answer += abcMap[j][indexList.index(i)]
        indexList[indexList.index(i)] = len(key) + 1

print(answer)