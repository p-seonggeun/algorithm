import sys
input = sys.stdin.readline
INF = 1e9
N, M = map(int, input().split())
graph = [[INF] * N for _ in range(N)]

for _ in range(M) :
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1

for i in range(N) :
    for j in range(N) :
        if i == j :
            graph[i][j] = 0

for k in range(N) :
    for a in range(N) :
        for b in range(N) :
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

answer = [0, INF]
for index, i in enumerate(graph) :
    if sum(i) < answer[1] :
        answer = [index + 1, sum(i)]

print(answer[0])