mainFile = r'Python\Algorithms\School encryption\Caesar\letter.txt'
afterPopular = r'Python\Algorithms\School encryption\Caesar\letterAfterPopular.txt'
dictionary = r'Python\Algorithms\School encryption\Caesar\findWords.txt'
afterSpaces = r'Python\Algorithms\School encryption\Caesar\spaced.txt'

f = open(mainFile, encoding='utf-8')
letter = str(f.read())
f.close()
nletter = ''
for i in range(len(letter)):
    nletter += letter[i]
letter = nletter

del nletter

abc = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я','\n']
abcRatio = [0 for i in range(len(abc))]
for i in letter:
    if i in abc:
        abcRatio[abc.index(i)] += 1

popularAbc = ['о','е','а','и','н','т','с','р','в','л']#,'к','м','д','п','у','я','ы','ь','г','з','б','ч','й','х','ж','ш','ю','ц','щ','э','ф','ё','ъ']
popularInLetter = ['*' for i in range(len(popularAbc))]

for i in range(len(popularAbc)):
    popularInLetter[i] = abc[abcRatio.index(max(abcRatio))]
    abcRatio[abcRatio.index(max(abcRatio))] = 0
for i in letter:
    if i in popularInLetter:
        i = popularAbc[popularInLetter.index(i)]

f = open(afterPopular, 'w', encoding='utf-8')
f.write(letter)
f.close()

#       abc = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
abcToChange = ['а','*','в','*','*','е','*','*','и','*','*','л','*','н','о','*','р','с','т','*','*','*','*','*','*','*','*','*','*','*','*','*','\n']
usedSymbs = []
for i in abcToChange:
    if i != '*':
        usedSymbs.append(i)
print(usedSymbs)

answer = ''
for i in letter:
    answer += abcToChange[abc.index(i)]

f = open(afterPopular, mode='w', encoding='utf-8')
f.write(f'{answer}\n{usedSymbs}')
f.close()

print("end")