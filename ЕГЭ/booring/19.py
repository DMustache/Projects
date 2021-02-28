A = [12, 8, 15, 23, 11, 4, 9, 22, 10, 15]
s = 0
n = 7
for i in range(9):
    if A[i] <= A[n]:
        s += A[i]
        t = A[i]
        A[i] = A[n]
        A[n] = t
        n = i % 3
print(s)