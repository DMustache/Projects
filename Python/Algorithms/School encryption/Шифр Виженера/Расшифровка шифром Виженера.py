abc = str(input())#'abcdefghijklmnopqrstuvwxyz'

abcMap = [['' for i in range(len(abc))] for j in range(len(abc))]
for i in range(len(abc)):
    for j in range(len(abc)):
        abcMap[i][j] = abc[(j+i)%len(abc)]
    print(*abcMap[i])
key = str(input())#'lemon'
chipher = str(input())#'lxfopvefrnhr'

answer = ''
for i in range(len(chipher)):
    answer += str(abcMap[abc.index(key[i % len(key)])][abcMap[abc.index(key[i % len(key)])][abc.index(chipher[i])]])
    print(answer[i], key[i % len(key)], chipher[i])
print(answer)