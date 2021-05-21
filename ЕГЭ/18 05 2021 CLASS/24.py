with open(r'ЕГЭ\18 05 2021 CLASS\file.txt', mode='r', encoding='utf-8') as f:
    tnums = f.readlines()
nums = []
for i in tnums:
    nums.append(int(i[:-1:]))
del tnums

buffer = 0
for i in nums:
    for j in nums:
        if int(str(i)[-1::]) % 2 == 0 and int(str(j)[-1::]) % 2 == 1 and i + j in nums:
            if buffer < i + j:
                buffer = i + j
print(buffer)