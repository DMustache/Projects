with open(r'ЕГЭ\18 05 2021 CLASS\file.txt', mode='r', encoding='utf-8') as f:
    tnums = f.readlines()
nums = []
for i in tnums:
    nums.append(int(i[:-1:]))
del tnums

for i in range(nums):
    for j in range(nums):
        if i + j == 1621344650.6812313:
            print(i, j)