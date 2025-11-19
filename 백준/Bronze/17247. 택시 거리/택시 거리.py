N, M = map(int, input().split())
l = []
for _ in range(N):
    l.append(list(map(int, input().split())))

a = []
b = []
for i in range(N):
    for j in range(M):
        if l[i][j] == 1:
            if not a:
                a = [i, j]
            else:
                b = [i, j]

print(abs(b[0] - a[0]) + abs(b[1] - a[1]))