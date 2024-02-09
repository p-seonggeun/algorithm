import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = []
d = [[0] * (m + 1) for _ in range(n + 1)]

for _ in range(n) :
    l.append(list(map(int, input().split())))

for i in range(1, n + 1) :
    for j in range(1, m + 1) :
        d[i][j] = l[i - 1][j - 1] + d[i][j - 1] + d[i - 1][j] - d[i - 1][j - 1]

k = int(input())
for _ in range(k) :
    i, j, x, y = map(int, input().split())
    print(d[x][y] - d[x][j - 1] - d[i - 1][y] + d[i - 1][j - 1])