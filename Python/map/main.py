import tkinter, random, os

numList = []
def createMap(MAP):
    mapsize = 50
    def adjacent_min(noise):
        output = []
        for i in range(len(noise) - 1):
            output.append(min(noise[i], noise[i + 1]))
        return output

    global numList
    for i in range(20):
        random.seed(i)
        noise = [random.randint(1, 2) for i in range(mapsize)]
        numList.append(adjacent_min(noise))

    for i in range(len(numList)):
        for j in range(len(numList[0])):
            if j == 0:
                MAP += '\n'

            if numList[i][j] == 1:
                MAP += '.'
            else:
                MAP += '#'

    return MAP

MAP = ''
MAP = createMap(MAP)



f = open(r'Python\map\txt.txt', mode='w')
f.write(MAP)
f.close()

command = r'notepad.exe Python\map\txt.txt'
os.system(command)