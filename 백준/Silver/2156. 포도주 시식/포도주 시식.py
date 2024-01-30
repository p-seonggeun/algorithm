import sys
input = sys.stdin.readline

n = int(input())
l = [0]
d = [[0, 0, 0] for _ in range(n + 1)]
for _ in range(n) :
    l.append(int(input()))

if n == 1 :
    print(l[1])
    exit(0)

d[1][0] = 0
d[1][1] = l[1]
d[1][2] = 0

for i in range(2, n + 1) :
    d[i][0] = max(d[i - 1][0], d[i - 1][1], d[i - 1][2])
    d[i][1] = max(d[i - 1][0] + l[i], d[i - 2][1] + l[i], d[i - 2][2] + l[i])
    d[i][2] = d[i - 1][1] + l[i]

d = sum(d, [])
print(max(d))