def toten(num):
    lght = len(num)
    ans = 0
    for i in range(0, lght):
        ans += int(num[i]) * (9 ** (lght - i - 1))
    return ans
num = 109418989131517142142
num = toten(str(num))
print(num, str(num).count('0'))