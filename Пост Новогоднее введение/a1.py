n = int(input())
for i in range(n):
    #p, q, k - Предел - p, Обязательно иметь в ряду - q, Умножение на k
    maxNum, toStep, multiple = map(int, input().split())
    numlist = [1, 2]
    multlist = [1]
    for i in range(toStep - 1):
        numlist.append(numlist[i - 2] + numlist[i - 1]) #pass

        if multlist[i] * multiple < toStep:
            multlist.append(i + 1)
        else:
            multlist.append(multlist[i - 2] + multlist[i - 1])
print(multlist[-1] + numlist[-1])
