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

popularAbc = ['о','е','а','и','н','т','с','р','в','л']#,'к','м','д','п','у','я','ы','ь','г','з','б','ч','й','х','ж','ш','ю','ц','щ','э','ф','ё','ъ']
popularInLetter = [' ' for i in range(len(popularAbc))]

for i in range(len(popularAbc)):
    popularInLetter[i] = abc[abcRatio.index(max(abcRatio))]
    abcRatio[abcRatio.index(max(abcRatio))] = 0
for i in letter:
    if i in popularInLetter:
        i = popularAbc[popularInLetter.index(i)]

f = open('Python\\Алгоритмы\\abstract classes\\Школьное Шифрование\\new.txt', 'w', encoding='utf-8')
f.write(letter)
f.close()

#       abc = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
abcToChange = [' ',' ',' ',' ','д',' ','й',' ',' ',' ',' ',' ','м',' ','о',' ',' ',' ',' ',' ',' ','ж',' ',' ','и',' ',' ',' ',' ',' ',' ','я']

for i in abcToChange:
    if abcToChange.count(i) > 1 and i != ' ':
        print(f'{i} в алфавите встречается {abcToChange.count(i)} раз')

for i in letter:
    if i in abc and abcToChange[abc.index(i)] != ' ':
        i = abcToChange[abc.index(i)]

with open('Python\\Алгоритмы\\abstract classes\\Школьное Шифрование\\findWords.txt', 'r', encoding='utf-8') as f:
    findWords = f.readlines()
findWords = [x.strip() for x in findWords]
f.close()

for word in findWords:
    letter = letter.replace(word, f' {word} ')

f = open('Python\\Алгоритмы\\abstract classes\\Школьное Шифрование\\newCOPY.txt', 'w', encoding='utf-8')
f.write(letter)
f.close()

print("end")