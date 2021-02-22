n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

counter = 0
for i in range(n):
    for j in range(n):
        if i != j and (lst[i] - lst[j]) % 17 == 0 and (lst[i] * lst[j]) % 3 == 0:
            counter += 1
print(counter)