from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(maps):
    answer = 0
    queue = deque()
    queue.append((0, 0))
    while queue :
        x, y = queue.popleft()
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) :
                if maps[nx][ny] == 1 :
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
    
    if maps[len(maps) - 1][len(maps[0]) - 1] == 1 :
        return -1
    return maps[len(maps) - 1][len(maps[0]) - 1]