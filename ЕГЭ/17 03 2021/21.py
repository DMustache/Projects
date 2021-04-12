def f(n, dump, c):
    if n * 2 <= dump and n * 2 != 30:
        return f(n * 2, dump, c + 1)
    if n * 3 <= dump and n * 3 != 30:
        return f(n * 3, dump, c + 1)
    if n + 1 == dump or n + 1 < dump and n + 1 != 30:
        return c + 1
print(f(2, 12, 0) + f(13, 39, 0))