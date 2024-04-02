from collections import deque
def bfs(x, time) :
    queue = deque()
    queue.append((x, time))
    while queue :
        x, time = queue.popleft()
        if x == k :
            return time
        
        for i in range(3) :
            if i == 0 :
                nx = x + 1
            elif i == 1 :
                nx = x - 1
            else :
                nx = x * 2
            if 0 <= nx <= 100000 :
                if not visited[nx] :
                    queue.append((nx, time + 1))
                    visited[nx] = True
            

n, k = map(int, input().split())
visited = [False] * 100001
print(bfs(n, 0))