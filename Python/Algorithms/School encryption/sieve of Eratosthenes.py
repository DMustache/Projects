def eratosthenes(num):
    sieve = [i for i in range(num + 1)]
    print(sieve)
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve
print(eratosthenes(1024))