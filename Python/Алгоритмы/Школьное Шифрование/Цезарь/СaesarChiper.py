abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

code = 'вшгшвылыешхдшцбюбдуфуьчшауауегуяву'
key = 'трамп'

def deChipher(code, shifter):
    global abc

    ans = ""
    for i in code:
        ans += abc[(abc.index(i) + shifter) % len(abc)]
    return ans

shifter = []
answer = []
for i in range(len(abc) // 2):
    if key in deChipher(code, i) and deChipher(code, i) not in answer:
        print(deChipher(code, i), i)
        answer.append(deChipher(code, i))
        shifter.append(i)

    if key in deChipher(code, i * (-1)) and deChipher(code, i * (-1)) not in answer:
        print(deChipher(code, i * (-1)), i * (-1))
        answer.append(deChipher(code, i * (-1)))
        shifter.append(i)

if len(answer) != 1:
    print('ERROR')
else:
    print(shifter[0])
    print(*answer)
print(len(abc))