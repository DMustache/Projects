# 1 - количество данных
# 4 - длинна кода расшифровки
# BD 1C BD 55 - код расшифровки
# 5 - длина и высота поля для взлома
# 1C BD 1C 55 55 - поле для взлома
# 55 55 55 1C 1C v
# E9 1C 55 55 E9
# BD 1C 1C 1C BD
# 55 BD E9 55 1C
n = 1
hackLen = 4
hack = ["BD", "1C", "BD", "55"]
codelistLen = 5
codeList = [
    ["1C", "BD", "1C", "55", "55"],
    ["55", "55", "55", "1C", "1C"],
    ["E9", "1C", "55", "55", "E9"],
    ["BD", "1C", "1C", "1C", "BD"],
    ["55", "BD", "E9", "55", "1C"]
]
posX, posY = 0, 0
for stepBrother in hack:
    for i in range(codelistLen):
        