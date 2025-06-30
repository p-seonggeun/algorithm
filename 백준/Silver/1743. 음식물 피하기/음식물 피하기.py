from collections import deque

N, M, K = map(int, input().split())
board = [['.' for _ in range(M)] for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    r -= 1
    c -= 1

    board[r][c] = '#'

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start):
    count = 0
    queue = deque()
    queue.append(start)

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M :
                if board[nx][ny] == '#':
                    count += 1
                    board[nx][ny] = '!'
                    queue.append((nx, ny))

    return count

answer = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == '#':
            answer = max(answer, bfs((i, j)))
print(answer)