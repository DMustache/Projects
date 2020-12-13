firstparam, secondparam = map(int, input().split())
firstdict = dict()
for i in range(firstparam - 1):
    firstpar, secpar = list(map(int,input().split()))
    if firstpar in firstdict:
        firstdict[firstpar].append(secpar)
    else:
        firstdict[firstpar] = [secpar]

secdict = dict()
secdict[1] = [1]
looper = 1

mainloop = True
while(mainloop):
    firstpar, looper = [], looper + 1
    for i in secdict[looper - 1]:
        if i in firstdict:
            firstpar += firstdict[i]
    if len(firstpar) <= 0:
        mainloop = False
    else:
        secdict[looper] = firstpar

listM = list(map(int, input().split()))
for j in listM:
    print(S3[em-1])