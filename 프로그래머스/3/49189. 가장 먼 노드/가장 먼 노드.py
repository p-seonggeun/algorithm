from collections import deque
def bfs(graph, v, visited) :
    queue = deque([v])
    visited[v] = 1
    while queue :
        p = queue.popleft()
        for i in graph[p] :
            if not visited[i] :
                visited[i] = visited[p] + 1
                queue.append(i)

def solution(n, edge):
    answer = 0
    l = [[] for i in range(n + 1)]
    visited = [0] * (n + 1)
    
    for i in edge :
        l[i[0]].append(i[1])
        l[i[1]].append(i[0])
    
    # for i in l :
    #     i.sort()
    #     print(i)
        
    bfs(l, 1, visited)
    
    answer = visited.count(max(visited))
    
    return answer