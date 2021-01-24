sum_of_road = 0
dif = 0
lowRange = 0

for i in range(5):
    line0, line1, line2 = map(int, input().split())
    sum_of_road += max(line0, line1, line2)
    tmp0 = (max(line0, line1) - min(line0, line1))
    tmp1 = (max(line1, line2) - min(line1, line2))
    tmp2 = (max(line0, line2) - min(line0, line2))

    if (line0 > 0 and line1 % 3 != 0 and line0 <= line1 and line0 <= line2):
        lowRange = tmp0
    elif (line1 > 0 and line0 % 3 != 0 and line1 <= line0 and line1 <= line2):
        lowRange = tmp1
    elif (line2 > 0 and line1 % 3 != 0 and line2 <= line1 and line2 <= line0):
        lowRange = tmp2

    if (lowRange != 0 or lowRange < 0):
        dif = lowRange

if (sum_of_road % 3 == 0 and dif == 0):
    print('Save me!')
elif (sum_of_road % 3 == 0 and dif != 0):
    print(sum_of_road - dif)
else:
    print(sum_of_road)