n, q = map(int, input().split())
S1 = dict()
for i in range(n - 1):
    a, b = list(map(int, input().split()))
    if a in S1:
        S1[a].append(b)
    else:
        S1[a] = [b]

S2 = dict()
S3 = [0 for i in range(n)]
S3[0] = 1
S2[1] = [1]
L = 1
while True:
    L = L + 1
    a = []
    for el in S2[L - 1]:
        if el in S1:
            a = a + S1[el]
    if len(a)>0:
        S2[L] = a
        tmp = len(a)
        for a1 in a:
            S3[a1 - 1] = tmp
    else:
        break

listM = list(map(int, input().split()))
for em in listM:
    print(S3[em - 1])