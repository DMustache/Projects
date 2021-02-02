from datetime import datetime

items = [2, 3, 5, 7, 11, 13, 17]

def bin_search(lst, x):
    i = 0
    j = len(lst)
    while i != j:
        m = (i + j) // 2
        if x == lst[m]:
            return m
        if x < lst[m]:
            j = m
        else:
            i = m + 1
    return None

lst = [1, 7, 19]
for i in range(3):
    bin_search(lst[i])

items = range(0, 10000000)
count = 100

start = datetime.now()

for n in range(1, count):
    bin_search(items, 777777)

delta = datetime.now() - start

totalMicroseconds = delta.seconds * 1000000 + delta.microseconds
print(totalMicroseconds / count)