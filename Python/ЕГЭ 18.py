y, x = map(int, input().split())
location = [list(map(int, input().split())) for i in range(y)]
cost = [[0] * x for i in range(y)]
road = [[""] * x for i in range(y)]
cost[0][0] = location[0][0]

for Xelem in range(1, x):
    cost[0][Xelem] = cost[0][Xelem - 1] + location[0][Xelem]
    road[0][Xelem] = road[0][Xelem - 1] + 'R'

for Yelem in range(1, y):
    cost[Yelem][0] = cost[Yelem - 1][0] + location[Yelem][0]
    road[Yelem][0] = road[Yelem - 1][0] + 'D'

for Yelem in range(1, y):
    for Xelem in range(1, x):
        cost[Yelem][Xelem] = max(cost[Yelem][Xelem -1], cost[Yelem - 1][Xelem]) + location[Yelem][Xelem]
        if cost[Yelem][Xelem - 1] > cost[Yelem - 1][Xelem] :
            road[Yelem][Xelem] = road[Yelem][Xelem - 1] + 'R'
        else :
            road[Yelem][Xelem] = road[Yelem - 1][Xelem] + 'D'
print(cost[-1][-1])
print(road[-1][-1])
