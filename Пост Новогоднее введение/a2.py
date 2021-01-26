def ForRow(codeList, posY, code, rangeColRow):
    for i in range(rangeColRow):
        if code == codeList[posY][i]:
            codeList[posY][i] = '-'
        elif i == rangeColRow:

        else:
            continue

def forColumn(codeList, posX, posY):


rangeColRow = 5
codeList = [
    ["1C", "BD", "1C", "55", "55"],
    ["55", "55", "55", "1C", "1C"],
    ["E9", "1C", "55", "55", "E9"],
    ["BD", "1C", "1C", "1C", "BD"],
    ["55", "BD", "E9", "55", "1C"]
]
hack = ["BD", "1C", "BD", "55"]
while play == True:

    if row:
        ForRow(codeList, posX, posY)
    else:
        forColumn(codeList, posX, posY)