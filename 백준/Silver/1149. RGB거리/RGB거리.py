import sys
input = sys.stdin.readline

n = int(input())
l = []
d = [[0, 0, 0] for _ in range(n)]
for i in range(n) :
    l.append(list(map(int, input().split())))

d[0][0] = l[0][0]
d[0][1] = l[0][1]
d[0][2] = l[0][2]

for i in range(1, n) :
    d[i][0] = min(d[i - 1][1], d[i - 1][2]) + l[i][0]
    d[i][1] = min(d[i - 1][0], d[i - 1][2]) + l[i][1]
    d[i][2] = min(d[i - 1][0], d[i - 1][1]) + l[i][2]

print(min(d[n - 1][0], d[n - 1][1], d[n - 1][2]))