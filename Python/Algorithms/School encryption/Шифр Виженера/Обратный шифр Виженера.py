sentence = str(input())
key = str(input())
newKey = ''
for i in range(len(sentence)):
    newKey += key[i % len(key)]
answer = ''
for i in range(len(sentence)):
    answer += f'{sentence[i]}({newKey[i]})'
print(answer)