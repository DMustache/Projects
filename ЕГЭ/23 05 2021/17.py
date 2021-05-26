lst = []
for i in range(1235, 7071):
    if sum([int(j) for j in str(i)]) % 3 == 0 and oct(i)[-2::] == '65':
        lst.append(i)
print(lst)
print(len(lst), sum(lst))