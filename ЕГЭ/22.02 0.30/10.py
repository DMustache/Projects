import itertools

counter = 0
abc = 'бильярдист'
lst = itertools.combinations_with_replacement(abc, 6)
for i in lst:
    if i[0] == 'ь':
        continue
    else:
        counter += 1
print(counter)