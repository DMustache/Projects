class boo():
    def impl(x, y):
        if x == 1 and y == 0:
            return 0
        else:
            return 1

    def remaind(x, y):
        if x % y == 0:
            return 1
        else:
            return 0

    def no(x):
        return int(not(x))

    def fc(x, y):
        return boo.impl(boo.remaind(x, a), (boo.no(boo.remaind(x, 8)) or boo.remaind(x, 30)))

    def equation(y, x, a):
        return boo.impl((120 == 2 * y + 3 * x), ((a < x) or (a < y)))

def simple(lst):
    ans = ''
    for i in range(len(lst)):
        ans += int(lst[i]) * 2 ** (i * (-1))
    return ans

def convertNum(base, s):
    s = s[::-1]
    ans = 0
    for i in range(len(s)):
        try:
            num = int(s[i])
            ans += num * base ** ((s.index(s[i])))
        except ValueError:
            ans += (ord(s[i])-87)* base ** ((s.index(s[i])))
    return ans

def booeq():
    b = True
    a = 0
    while b:
        a += 1
        lst = [i for  i in range(1, 512)]
        for i in range(len(lst)):
            if boo.fc(lst[i], a):
                continue
            else:
                lst[i] = 0
        if 0 in lst:
            continue
        else:
            print(a)
            b = False

def eq():
    b = True
    a = 0
    while b:
        a += 1
        lst = [i for  i in range(1, 512)]
        for i in range(len(lst)):
            for j in range(len(lst)):
                if boo.equation(lst[i], lst[j], a):
                    continue
                else:
                    lst[i] = 0
            if 0 in lst:
                continue
            else:
                print(a)
                b = False
