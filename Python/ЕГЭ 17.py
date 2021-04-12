def delimiters(num):
    tmp = 0
    for i in range(num -1, 1, -1):
        if num % i == 0:
            tmp += 1

            if tmp == 17:
                return True

    if tmp == 17:
        return True
    else:
        return False

lst = []
for i in range(30001, 70000):
    if delimiters(i) == True:
        lst.append(i)
print(min(lst), len(lst))