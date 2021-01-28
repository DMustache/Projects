Alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

def Encrypt(word):
    global NewAlphabet, Alphabet
    ans = ''
    for i in word:
        ans += NewAlphabet[Alphabet.index(i)]
    return ans

word = input()
Fpart, Spart = map(int, input().split())

codeList = ['','','','']
for symbol in range(0, Fpart):
    codeList[1] += Alphabet[symbol]

for symbol in range(Fpart, (Fpart * 2 + (Spart // 2) + 1) // 2):
    codeList[0] += Alphabet[symbol]

windex = ((Fpart * 2 + (Spart // 2) + 1) // 2)
while len(codeList[3]) != len(codeList[0]):
    codeList[3] += Alphabet[windex]
    windex += 1

for symbol in range(Fpart + (Spart // 2) + 1, len(Alphabet)):
    codeList[2] += Alphabet[symbol]

NewAlphabet = ''
for lst in range(4):
    NewAlphabet += codeList[lst]
NewAlphabet *= 2

print(Encrypt(word))