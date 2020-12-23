t = 900
arr = []
c = 0
for i in range(t):
    arr.append(i)
for j in arr:
    if str(j).count("9") == 2:
        c+=1
print(c/t)
