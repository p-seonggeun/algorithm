import sys
from collections import deque
input = sys.stdin.readline
N, L, R = map(int, input().split())
l = []

for _ in range(N) :
    l.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

def bfs(x, y, k) :
    flag = False
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N :
                if visited[nx][ny] : continue
                if L <= abs(l[x][y] - l[nx][ny]) <= R :
                    flag = True
                    board[x][y] = k
                    board[nx][ny] = k
                    team.add(k)
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
    return flag

while True :
    board = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    f = False
    team = set()

    tem = 1
    for i in range(N) :
        for j in range(N) :
            if not visited[i][j] :
                if bfs(i, j, tem) :
                    f = True
            tem += 1
    
    if f :
        answer += 1
        for k in list(team) :
            s = 0
            cnt = 0

            for i in range(N) :
                for j in range(N) :
                    if board[i][j] == k :
                        s += l[i][j]
                        cnt += 1
            
            temp = s // cnt

            for i in range(N) :
                for j in range(N) :
                    if board[i][j] == k :
                        l[i][j] = temp  
    else : 
        break

print(answer)