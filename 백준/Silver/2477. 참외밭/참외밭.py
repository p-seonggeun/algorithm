K = int(input())
east = []
west = []
north = []
south = []
d = []
dis = []
for _ in range(6):
    a, b = map(int, input().split())
    if a == 1:
        east.append(b)
    elif a == 2:
        west.append(b)
    elif a == 3:
        south.append(b)
    elif a == 4:
        north.append(b)

    d.append(a)
    dis.append(b)

if len(east) == 2 and len(south) == 2:
    target = [1, 3]
elif len(north) == 2 and len(east) == 2:
    target = [4, 1]
elif len(north) == 2 and len(west) == 2:
    target = [2, 4]
else:
    target = [3, 2]

d.append(d[0])
dis.append(dis[0])

index = 0
for i in range(len(d) - 1):
    if d[i] == target[0] and d[i + 1] == target[1]:
        index = i

small = dis[index] * dis[index + 1]
big = max(east + west) * max(south + north)

print((big - small) * K)
