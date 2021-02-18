abc = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я','\n']

f = open(r'Python\Algorithms\School encryption\Caesar\letter.txt', encoding='utf-8', mode='r')
letter = f.read()
f.close()

letterRatio = [0 for i in range(len(abc))]
for i in letter:
    letterRatio[abc.index(i)] += 1
popularInWorld = ['о','е','а','и','н','т','с','р','в','л']

popularInLetter = []
for i in range(len(popularInWorld)):
    popularInLetter.append(abc.index(max(letterRatio)))
    letterRatio[letterRatio.index(max(letterRatio))] = 0

print(popularInWorld)
print(popularInLetter)

abcToChange = ['*' for i in range(len(abc))]