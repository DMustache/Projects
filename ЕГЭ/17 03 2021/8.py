import itertools
lst = [chr(i) for i in range(ord('А'), ord("Я"))]
lst.pop(lst.index("В"))
ans = itertools.permutations(lst, "В", 3)
print(ans)