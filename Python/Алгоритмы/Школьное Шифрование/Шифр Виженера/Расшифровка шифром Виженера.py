abc = 'abcdefghijklmnopqrstuvwxyz'

abcMap = [['' for i in range(len(abc))] for j in range(len(abc))]
for i in range(len(abc)):
    for j in range(len(abc)):
        abcMap[i][j] = abc[(j+i)%len(abc)]
key = 'lemon'
chipher = 'lxfopvefrnhr'

newKey = ''
for i in range(len(chipher)):
    newKey += key[i % len(key)]

answer = ''
for i in range(len(chipher)):
    answer += str(abcMap[abcMap.index(newKey[i])][abcMap.index(chipher[i])])
print(answer)