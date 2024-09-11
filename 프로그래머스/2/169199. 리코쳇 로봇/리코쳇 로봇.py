from collections import deque
def solution(board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def move(x, y, i) :
        while True :
            x += dx[i]
            y += dy[i]
            if x < 0 or x >= r or y < 0 or y >= c or board[x][y] == 'D' :
                break
        x -= dx[i]
        y -= dy[i]
        return [x, y]
    
    def bfs(x, y, c) :
        queue = deque()
        queue.append((x, y, c))
        
        while queue :
            x, y, c = queue.popleft()
            for i in range(4) :
                nx, ny = move(x, y, i)
                if not visited[nx][ny] :
                    if board[nx][ny] == 'G' :
                        return c + 1
                    visited[nx][ny] = True
                    queue.append((nx, ny, c + 1))
        
        return -1
                
    answer = 0
    r, c = len(board), len(board[0])
    visited = [[False for _ in range(c)] for _ in range(r)]
    
    for i in range(r) :
        for j in range(c) :
            if board[i][j] == 'R' :
                t = bfs(i, j, 0)
                if t == -1 : return -1
                else : return t
            
    return answer