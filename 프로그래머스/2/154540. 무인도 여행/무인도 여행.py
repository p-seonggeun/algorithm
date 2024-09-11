from collections import deque
def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs(x, y) :
        t = 0
        queue = deque()
        queue.append((x, y))
        t += int(maps[x][y])
        while queue :
            x, y = queue.popleft()
            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) :
                    if maps[nx][ny] != 'X' and visited[nx][ny] == False :
                        visited[nx][ny] = True
                        t += int(maps[nx][ny])
                        queue.append((nx, ny))
        return t
                        
    answer = []
    t = []
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    
    for i in range(len(maps)) :
        for j in range(len(maps[i])) :
            if maps[i][j] != 'X' :
                t.append((i, j))
    
    if t :
        for i in t :
            if visited[i[0]][i[1]] == False :
                visited[i[0]][i[1]] = True
                answer.append(bfs(i[0], i[1]))
    else :
        answer = [-1]
    answer.sort()
    return answer