import itertools

counter = 0
abc = ['в','н','о','д','у','ш','е','сть']
lst = itertools.permutations(abc, len(abc))

print(len(list(lst)))
for i in lst:
    print(i)
    print(i.index('д'), i.index('у'), i.index('ш'), i.index('е'))
    if i.index('д') < 4 and i.index('у') < 4 and i.index('ш') < 4 and i.index('е') < 4:
        print(i)
        counter += 1
print(counter)