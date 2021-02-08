abc = 'abcdefghijklmnopqrstuvwxyz'

def abcLineDechipher(line, symbol):
    for i in line:
        if i == symbol:
            


abcMap = [['' for i in range(len(abc))] for j in range(len(abc))]
for i in range(len(abc)):
    for j in range(len(abc)):
        abcMap[i][j] = abc[(j+i)%len(abc)]
    print(*abcMap[i])

key = 'lemon'
sentence = 'lxfopvefrnhr'
newKey = ''
for i in range(len(sentence)):
    newKey += key[i % len(key)]

chipher = ''
for i in range(len(sentence)):
    chipher += abcMap[abc.index(newKey[i])][abcMap[abc.index(newKey[i])].index(sentence[i])]
    print(abcMap[abc.index(newKey[i])][abcMap[abc.index(newKey[i])].index(sentence[i])])
print(chipher)