def filter_list(l):
    l = [l[i] for i in len(l) if type(l[i]) is int]
    return l
print(filter_list([1,2,'a','b']))