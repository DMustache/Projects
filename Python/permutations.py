sz = 0
sz = int(input())
src = list(map(int, input().split()))
src.sort()
n = int(input())
lst = []

for i in range(2 ** sz):
    cur = (f'{bin(i)[2:]:0>{sz}}')
    curlist = []
    if (cur.count('1') == n):
        for j in range(len(cur)):
            if (cur[j] == '1'):
                curlist.append(src[j])
        lst.append(curlist)
lst.sort()
for i in lst:
    print(*i)