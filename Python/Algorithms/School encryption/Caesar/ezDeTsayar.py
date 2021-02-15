def abcCuter(keyF, keyS):
    global abc

    abcRecharger = ['','','','']
    for i in range(0, keyF, 1):
        abcRecharger[1] += abc[i]

    for i in range(keyF, (keyF + keyS+ 1) // 2, 1):
        abcRecharger[0] += abc[i]

    for i in range((keyF + keyS+ 1) // 2, keyS+ 1, 1):
        abcRecharger[3] += abc[i]

    for i in range(keyS+ 1, len(abc), 1):
        abcRecharger[2] += abc[i]
    answer = ''

    for i in abcRecharger:
        answer += i
    return answer
abc = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
f = open(r'Python\Algorithms\School encryption\Caesar\try.txt',mode='w',encoding='utf-8')

letter = 'ущбдпьущхфзфивсдсдсдсд'#str(input())

for tryF in range(32):
    for tryS in range(tryF+1,32):
        keyF, keyS = tryF, tryS#map(int, input().split())

        NewAlphabet = abcCuter(keyF, keyS)
        f.write(f'{keyF} {keyS} {NewAlphabet}\n')

        abcRecharger = ''
        for i in NewAlphabet:
            abcRecharger += i

        answer = ''
        for i in letter:
            answer += abcRecharger[abc.index(i)]
        f.write(f'{answer}\n\n')
f.close()