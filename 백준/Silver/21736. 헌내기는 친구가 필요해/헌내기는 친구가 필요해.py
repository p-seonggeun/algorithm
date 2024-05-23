from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y) :
    global answer
    queue = deque()
    queue.append((x, y))
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M :
                if campus[nx][ny] == 'O' or campus[nx][ny] == 'P' :
                    if campus[nx][ny] == 'P' :
                        answer += 1
                    campus[nx][ny] = 'X'
                    queue.append((nx, ny))

def check() :
    for i in range(N) :
        for j in range(M) :
            if campus[i][j] == 'I' :
                bfs(i, j)
                return

N, M = map(int, input().split())
campus = []
answer = 0
for _ in range(N) :
    campus.append(list(input()))

check()
if answer == 0 : print("TT")
else : print(answer)
