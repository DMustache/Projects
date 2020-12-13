firstparam, secondparam = map(int, input().split())
firstdict = dict()
for i in range( firstparam - 1):
    firstpar, secpar = list(map(int, input().split()))
    if firstpar in firstdict:
        firstdict[firstpar].append(secpar)
    else:
        firstdict[firstpar] = [secpar]

secdict = dict()
thirddict = [0 for i in range( firstparam)]
thirddict[0] = 1
secdict[1] = [1]
looper = 1
while True:
    looper = looper + 1
    firstpar = []
    for i in secdict[looper - 1]:
        if i in firstdict:
            firstpar = firstpar + firstdict[i]
    if len(firstpar)>0:
        secdict[looper] = firstpar
        tmp = len(firstpar)
        for a1 in firstpar:
            thirddict[a1 - 1] = tmp
    else:
        break

listM = list(map(int, input().split()))
for em in listM:
    print(thirddict[em - 1])