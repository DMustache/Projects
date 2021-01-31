from itertools import repeat

f = open('Python\\Алгоритмы\\abstract classes\\Школьное Шифрование\\letter.txt', encoding='utf-8')
letter = str(f.read())
f.close()
nletter = ''
for i in range(len(letter)):
    nletter += letter[i]
letter = nletter

del nletter

abc = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
abcRatio = [0 for i in range(len(abc))]

for i in letter:
    if i in abc:
        abcRatio[abc.index(i)] += 1

popularAbc = ['о','е','а','и','н','т','с','р','в','л']
popularInLetter = [0 for i in range(len(popularAbc))]

for i in range(len(popularAbc)):
    popularInLetter[i] = abc[abcRatio.index(max(abcRatio))]
    abcRatio[abcRatio.index(max(abcRatio))] = 0

for i in letter:
    if i in popularInLetter:
        i = popularAbc[popularInLetter.index(i)]

print(letter)