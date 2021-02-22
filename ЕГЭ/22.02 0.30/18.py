A = [6, 14, 25, 43, 37, 21, 15, 18, 24, 30]
s = 0
n = 5
for i in range(9):
    if (A[i] >= A[n]):
        s += A[i]
        t = A[i]
        A[n] = t
        n = i
print(s)