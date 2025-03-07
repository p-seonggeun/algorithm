import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())

board = []
for _ in range(N) :
    board.append(list(map(int, input().split())))

def bfs(i, j) :
    result = 0
    queue = deque()
    queue.append((i, j))
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M :
                if board[nx][ny] == 1 :
                    board[nx][ny] = 2
                    queue.append((nx, ny))
                    result += 1
    
    if result == 0 :
        return 1
    else :
        return result

answer = 0
m = 0
for i in range(N) :
    for j in range(M) :
        if board[i][j] == 1 :
            answer += 1
            m = max(m, bfs(i, j))

print(answer)
print(m)