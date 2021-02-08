import math
abc = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
abcToChange = [' ',' ',' ',' ','д',' ','й',' ',' ',' ',' ',' ','м',' ','о',' ',' ',' ',' ',' ',' ','ж',' ',' ','и',' ',' ',' ',' ',' ',' ','я']


for i in abcToChange:
    if abcToChange.count(i) > 1 and i != ' ':
        i = input(f'Замените {i}')

letter = 'оутштмюяхвуфмхжюуъгхмъсюжхявжятждоможясювйухуъйцжоьввум'

for i in letter:
    if i in abc and abcToChange[abc.index(i)] != ' ':

print(math.factorial(len(abc)))