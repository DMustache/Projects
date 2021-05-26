with open(r'ЕГЭ\23 05 2021\data.txt', mode='r', encoding='utf-8') as f:
    data = f.readlines()

data = [i.strip() for i in data]
fill, users = int(data[0][0:len('100000')]), int(data[0][len('100000 '):])
data.remove(f'{fill} {users}')
data = [int(i) for i in data]
data.sort()

acc = 0
for i in range(0, len(data), 1):
    for j in range(len(data), 0, -1):
        try:
            fill -= max(data)
            tmp = max(data)
            data.remove(max(data))
            acc += 1

            fill -= min(data)
            tmp = min(data)
            data.remove(min(data))
            acc += 1
        except ValueError:
            print(acc, tmp)
            break