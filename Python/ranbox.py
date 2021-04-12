import random

users = open(r'Python\names.txt', encoding='utf-8', mode='r').readlines()

for i in range(len(users)):
    users[i] = users[i][:-1]

print(*users)

inputed = open(r'Ppython\input.txt', encoding='utf-8', mode='w')
myname = str(input())
while len(users) != 1 or myname != '0':
    tmp = users[random.randint()]
    if tmp[:-1] == myname:
        while tmp[:-1] != myname:
            tmp = users[random.randint()]
    inputed.writelines(f'{myname} - {tmp}')
    for i in users:
        if tmp in i:
            i = ''
    