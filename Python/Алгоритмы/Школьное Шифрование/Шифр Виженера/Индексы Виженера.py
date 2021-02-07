abc = input().split()

abcMap = [['' for i in range(len(abc))] for j in range(len(abc))]
for i in range(len(abc)):
    for j in range(len(abc)):
        abcMap[i][j] = abc[(j+i)%len(abc)]

codeLen = int(input())
indexes = []
for i in range(codeLen):
    indexes.append([int(j) for j in input().split()])
    print(indexes)

answer = []
for i in range(len(indexes)):
    answer.append(abcMap[indexes[i][0]][indexes[i][1]])

for i in answer:
    print(*i)