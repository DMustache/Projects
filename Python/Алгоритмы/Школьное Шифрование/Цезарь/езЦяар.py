abc = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

letter = 'мамасобираетсынуобедвшколу'#str(input())

keyF, keyS = 8, 16#map(int, input().split())

def abcCuter(keyF, keyS):
    global abc

    abcRecharger = ['','','','']
    for i in range(0, keyF, 1):
        abcRecharger[1] += abc[i]

    for i in range(keyF, keyF + (keyS - keyF) // 2 + 1, 1):
        abcRecharger[0] += abc[i]

    for i in range(keyF + (keyS - keyF) // 2 + 1, keyS + 1, 1):
        abcRecharger[3] += abc[i]

    for i in range(keyS + 1, len(abc), 1):
        abcRecharger[2] += abc[i]
    answer = ''

    for i in abcRecharger:
        answer += i
    return answer

NewAlphabet = abcCuter(keyF, keyS)

abcRecharger = ''
for i in NewAlphabet:
    abcRecharger += i

answer = ''
for i in letter:
    answer += abcRecharger[abc.index(i)]

f = open(r'C:\Users\Dmitry\Documents\Projects\Python\Алгоритмы\Школьное Шифрование\Цезарь\new.txt',mode='w',encoding='utf-8')
f.write(answer)