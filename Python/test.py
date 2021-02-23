lst = [1 for i in range(30)]
newLst = lst
print(newLst)
newLst[1] = 0
newLst.pop([1])
print(newLst())
passer = True
while newLst != [2, 1, 1]:
	while passer == True:
		for i in range(len(newLst - 3)):
			if newLst[i] == 1 and newLst[i + 1] == 1 and newLst[i + 2] == 1:
				newLst.pop([i])
				newLst.pop([i + 1])
				newLst.pop()
