from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y, maps, visited, r, c) :
    queue = deque()
    queue.append((x, y))
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c :
                if visited[nx][ny] == False :
                    visited[nx][ny] = True
                    if maps[nx][ny] == 'E' :
                        return maps[x][y] + 1
                    if maps[nx][ny] != 'X' :
                        maps[nx][ny] = maps[x][y] + 1
                        queue.append((nx, ny))
    return -1
                    
def solution(maps):

    answer = 0
    r, c = len(maps), len(maps[0])
    
    visited = [[False for _ in range(c)] for _ in range(r)]
    map1, map2 = [], []
    for i in range(r) :
        t1, t2 = [], []
        for j in range(c) :
            if maps[i][j] == 'X' :
                t1.append('X')
                t2.append('X')
            elif maps[i][j] == 'S' :
                t1.append('S')
                t2.append(0)
            elif maps[i][j] == 'L' :
                t1.append('E')
                t2.append('S')
            elif maps[i][j] == 'E' :
                t1.append(0)
                t2.append('E')
            else : 
                t1.append(0)
                t2.append(0)
        
        map1.append(t1)
        map2.append(t2)
        
    t = 0

    for i in range(r) :
        for j in range(c) :
            if map1[i][j] == 'S' :
                map1[i][j] = 0
                visited[i][j] = True
                t = bfs(i, j, map1, visited, r, c)
            if t == -1 :
                return -1
    answer += t
            
    visited = [[False for _ in range(c)] for _ in range(r)]
    for i in range(r) :
        for j in range(c) :
            if map2[i][j] == 'S' :
                visited[i][j] = True
                map2[i][j] = 0
                t = bfs(i, j, map2, visited, r, c)
            if t == -1 :
                return -1
    answer += t
    
    
    return answer
