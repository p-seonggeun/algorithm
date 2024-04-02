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
                nx = 2 * x
                ntime = time
            elif i == 1 :
                nx = x - 1
                ntime = time + 1
            else :
                nx = x + 1
                ntime = time + 1
            if 0 <= nx <= 100000 :
                if not visited[nx] :
                    queue.append((nx, ntime))
                    visited[nx] = 1

n, k = map(int, input().split())
visited = [0] * 100001
print(bfs(n, 0))