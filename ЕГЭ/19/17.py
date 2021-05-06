def convert(num):
    to_base = 7
    from_base = 10
    # first convert to decimal number
    n = int(num, from_base) if isinstance(num, str) else num
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while n > 0:
        n,m = divmod(n, to_base)
        res += alphabet[m]
    return res[::-1]

lst = []
for i in range(1273, 6438):
    end = convert(i)
    end = end[-3] + end[-2] + end[-1]
    if i % 5 == 0 and end == '125':
        lst.append(i)
print(len(lst), sum(lst))