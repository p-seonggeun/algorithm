from itertools import combinations
def spreadVirus() :
    visited = [[0 * i for i in range(m)] for _ in range(n)]
    for x, y in virus :
        visited[x][y] = 1
        dfs(x, y, visited)
    
    cnt = 0
    
    for i in range(n) :
        for j in range(m) :
            if board[i][j] == 0 and visited[i][j] == 0 :
                cnt += 1
    return cnt

def dfs(x, y, visited) :
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m :
            if visited[nx][ny] != 1 and board[nx][ny] != 1 : 
                visited[nx][ny] = 1
                dfs(nx, ny, visited)

n, m = map(int, input().split())
answer = 0
board = []
for _ in range(n) :
    board.append(list(map(int, input().split())))

wall = []
virus = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n) :
    for j in range(m) :
        if board[i][j] == 0 :
            wall.append([i, j])
        if board[i][j] == 2 :
            virus.append([i, j])

for i in list(combinations(wall, 3)) :
    for x, y in i :
        board[x][y] = 1
    answer = max(answer, spreadVirus())
    for x, y in i :
        board[x][y] = 0

print(answer)