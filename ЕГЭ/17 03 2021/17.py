def delimiter(num):
    ans = 0
    for i in range(2, num - 1):
        if num % i == 0:
            ans += 1
        if ans == 3:
            return ans
    return ans
lst = []
for i in range(10001, 50000):
    if delimiter(i) == 3:
        lst.append(i)

print(min(lst), len(lst))

#! Не робит
#! Робит