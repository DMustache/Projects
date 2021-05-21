lst = []
for i in range(123456, 234568):
    if i % sum([int(j) for j in str(i)]) == 0:
        lst.append(i)
print(len(lst), min(lst))

#! +1
#! *3
#! >= 88
#! 1 ≤ S ≤ 81
