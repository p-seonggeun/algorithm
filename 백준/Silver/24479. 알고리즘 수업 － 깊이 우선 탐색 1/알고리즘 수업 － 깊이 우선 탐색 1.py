import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for x in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    i.sort()

k = 1
def dfs(r):
    global k
    visited[r] = k
    k += 1
    for i in graph[r]:
        if not visited[i] :
            dfs(i)

dfs(r)

for i in range(1, n + 1):
    print(visited[i])
