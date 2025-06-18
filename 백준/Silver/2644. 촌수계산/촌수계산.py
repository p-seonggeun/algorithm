from collections import deque

n = int(input())
a, b = map(int, input().split())  # 촌수 계산해야하는 번호
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range (n + 1)]

for _ in range(m):
    x, y = map(int, input().split())  # x는 부모, y는 자식
    graph[x].append(y)
    graph[y].append(x)

def bfs(start, end) :
    queue = deque()
    queue.append((start, 0))
    visited[start] = True

    while queue:
        current, chon = queue.popleft()

        if current == end :
            return chon

        for i in graph[current]:
            if not visited[i] :
                visited[i] = True
                queue.append((i, chon + 1))

    return -1

print(bfs(a, b))