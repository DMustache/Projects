lst = []
for i in range(1490, 8132):
    if sum([int(j) for j in str(i)]) % 7 == 0 and oct(i)[-3::] != 'D92':
        lst.append(i)
print(lst)
print(len(lst), max(lst))