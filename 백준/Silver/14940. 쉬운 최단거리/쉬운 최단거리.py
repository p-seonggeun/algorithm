from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y) :
    queue = deque()
    queue.append((x, y))
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m :
                if board[nx][ny] == 1 and visited[nx][ny] == 0 :
                    visited[nx][ny] = 1
                    board[nx][ny] = board[x][y] + 1
                    queue.append((nx, ny))

def check() :
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                board[i][j] = 0
                return bfs(i, j)

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = []
visited = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(n) :
    board.append(list(map(int, input().split())))

check()

for i in range(n) :
    for j in range(m) :
        if visited[i][j] == 0 and board[i][j] == 1 :
            print(-1, end = " ")
        else :
            print(board[i][j], end = " ")
    print()
