abc = 'abcdefghijklmnopqrstuvwxyz'

abcMap = [['' for i in range(len(abc))] for j in range(len(abc))]
for i in range(len(abc)):
    for j in range(len(abc)):
        abcMap[i][j] = abc[(j+i)%len(abc)]

key = 'lemon'
sentence = str(input())
newKey = ''
for i in range(len(sentence)):
    newKey += key[i % len(key)]
print(newKey)
chipher = ''
for i in range(len(sentence)):
    chipher += abcMap[abc.index(newKey[i])][abc.index(sentence[i])]
print(chipher)