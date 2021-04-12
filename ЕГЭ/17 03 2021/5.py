def toten(num):
    lght = len(num)
    ans = 0
    for i in range(0, lght):
        ans += int(num[i]) * (2 ** (lght - i - 1))
    return ans

def step2(num):
    if num.count('1') == num.count('0'):
        num += num[-1]
    else:
        num += min(num)

num = '104'
while True:
    for i in range(3):
        step2(num)
    ans = num
    ans = toten(str(num))
    if ans % 4 != 0:
        str(int(num) + 1)
    else:
        break
print(ans)