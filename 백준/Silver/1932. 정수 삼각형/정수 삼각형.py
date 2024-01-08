n = int(input())
l = []
result = 0
d = [[0] * (i + 1) for i in range(n)]
for _ in range(n) :
    l.append(list(map(int, input().split())))
d[0][0] = l[0][0]

for i in range(0, n - 1) :
    for j in range(len(l[i])) :
        d[i + 1][j] = max(d[i + 1][j], d[i][j] + l[i + 1][j])
        d[i + 1][j + 1] = max(d[i + 1][j + 1], d[i][j] + l[i + 1][j + 1])

result = max(d[n - 1])
print(result)