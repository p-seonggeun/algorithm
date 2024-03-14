n = int(input())
d = [[0, 0] for _ in range(n + 1)]
l = list(map(int, input().split()))

for i in range(len(l)) :
    if l[i] == 1 :
        d[i + 1][0] = max(d[i][0] + 1, 0)
        d[i + 1][1] = max(d[i][1] - 1, 0)
    else :
        d[i + 1][0] = max(d[i][0] - 1, 0)
        d[i + 1][1] = max(d[i][1] + 1, 0)

result = 0

for i in d :
    result = max(result, max(i))

print(result)