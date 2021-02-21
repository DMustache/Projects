import random

numList = []
MAP = ''
def noiser02():
    mapsize = 50
    def adjacent_min(noise):
        output = []
        for i in range(len(noise) - 1):
            output.append(min(noise[i], noise[i + 1]))
        return output

    global numList, MAP
    for i in range(50):
        random.seed(i)
        noise = [random.randint(1, 2) for i in range(mapsize)]
        numList.append(adjacent_min(noise))
    counter = 0
    for i in range(len(numList)):
        for j in range(len(numList)):
            try:
                if numList[i][j] == 1:
                    MAP += '.'
                    if len(MAP) % 50 + counter == 0:
                        counter += 1
                        MAP += '\n'
                else:
                    MAP += '#'
                    if len(MAP) % 50 + counter == 0:
                        counter += 1
                        MAP += '\n'
            except IndexError:
                continue
    return MAP


print(noiser02())
