from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y, n, m, maps) :
    queue = deque()
    queue.append((x, y))
    
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m :
                if maps[nx][ny] == 1 :
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    
    bfs(0, 0, n, m, maps)
    
    answer = maps[n - 1][m - 1]
    if answer == 1 :
        return -1
    
    
    return answer