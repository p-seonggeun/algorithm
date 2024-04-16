import heapq, sys
input = sys.stdin.readline
INF = 1e9

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M) :
    a, b, c = map(int, input().split())    
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start) :
    queue = []
    heapq.heappush(queue, (0, start)) # 거리, 노드
    distance[start] = 0
    while queue :
        dist, now = heapq.heappop(queue)
        if distance[now] < dist :
            continue
        for i in graph[now] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

dijkstra(1)

print(distance[N])