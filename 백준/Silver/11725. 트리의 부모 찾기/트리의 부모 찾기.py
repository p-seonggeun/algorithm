import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())
l = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
dict = {}

for _ in range(n - 1) :
    node1, node2 = map(int, input().split())
    l[node1].append(node2)
    l[node2].append(node1)

def dfs(graph, v, visited) :
    visited[v] = True
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)
        else :
            dict[v] = i

dfs(l, 1, visited)

for i in range(2, n + 1) :
    print(dict[i])