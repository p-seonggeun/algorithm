# 2차원 5 * 5 배열을 1차원으로 바꿀 때
# (0, 0) -> 0 * 5 + 0 -> 0
# (1, 1) -> 1 * 5 + 1 -> 6
# 1차원 배열을 2차원 5 * 5 배열로 바꿀 때
# 0 -> (0 // 5, 0 % 0) -> 0
# 6 -> (6 // 5, 6 % 5) -> (1, 1)
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y) :
    queue = deque()
    v = [[0] * 5 for _ in range(5)]
    queue.append((x, y))
    v[x][y] = 1
    cnt = 1

    while queue :
        x, y = queue.popleft()
        for i, j in zip(dx, dy) :
            nx, ny = x + i, y + j
            if 0 <= nx < 5 and 0 <= ny < 5 and v[nx][ny] == 0 and visited[nx][ny] == 1 :
                queue.append((nx, ny))
                v[nx][ny] = 1
                cnt += 1
    return cnt == 7

def check() :
    for i in range(5) :
        for j in range(5) :
            if visited[i][j] == 1 :
                return bfs(i, j)

def dfs(n, cnt, scnt) :
    global answer
    if cnt > 7 :
        return
    if n == 25 :
        if cnt == 7 and scnt >= 4 :
            if check() :
                answer += 1
        return
    
    visited[n // 5][n % 5] = 1 # 포함하는 경우
    dfs(n + 1, cnt + 1, scnt + int(arr[n // 5][n % 5] == 'S'))
    visited[n // 5][n % 5] = 0 # 원상복구
    dfs(n + 1, cnt, scnt) # 포함하지 않는 경우


arr = [input().rstrip() for _ in range(5)]
answer = 0
visited = [[0] * 5 for _ in range(5)]
dfs(0, 0, 0)
print(answer)