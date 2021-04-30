def imp(n, m):
    if n == 1 and m == 0:
        return 0
    else:
        return 1

def fuck(k, n, a):
    if (5 * k + 7 * n <= 108 and (k <= a and n < a)) and imp((5 * k + 7 * n <- 108),(k <= a and n < a)):
        return 1
    else:
        return 0
minimal = 500
k = [i for i in range(1, 21)]
n = [i for i in range(1, 15)]
b = False
a = 0
i = 0
while b == False:
    if fuck(k[i], n[i], a+i):
        b = False