import math, random
abc = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
abcToChange = [' ',' ',' ',' ','д',' ','й',' ',' ',' ',' ',' ','м',' ','о',' ',' ',' ',' ',' ',' ','ж',' ',' ','и',' ',' ',' ',' ',' ',' ','я']

def notUsedABC():
    nonAbcToChange = []
    global abc, abcToChange
    for i in range(len(abc)):
        if abc[i] not in abcToChange:
            nonAbcToChange.append(abc[i])
    return nonAbcToChange

def notDetected():
    global abcToChange
    for i in range(len(abcToChange)):
        if abcToChange.count(abcToChange[i]) > 1:
            abcToChange[i] == ' '
    return nonAbcToChange

while abcToChange.count(' ') == 0:
    for i in range(len(abc)):
        nonAbcToChange = notUsedABC()
        abcToChange[i] = nonAbcToChange[random.randint(0, len(nonAbcToChange))]
        notDetected()

letter = 'оутштмюяхвуфмхжюуъгхмъсюжхявжятждоможясювйухуъйцжоьввум'

for i in letter:
    if i in abc and abcToChange[abc.index(i)] != ' ':
        newLetter += abcToChange[abc.index(i)]
