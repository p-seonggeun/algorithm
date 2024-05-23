from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(t) :
    queue = deque()
    for i in t :
        queue.append(i)
    while queue :
        x, y = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M :
                if board[nx][ny] == 0 :
                    board[nx][ny] = board[x][y] + 1
                    queue.append((nx, ny))

def check() :
    global day
    for i in range(N) :
        for j in range(M) :
            if board[i][j] == 0 :
                return 0
            day = max(day, board[i][j])
    return day

import sys
input = sys.stdin.readline
M, N = map(int, input().split())
board = []
for _ in range(N) :
    board.append(list(map(int, input().split())))
day = 0
tomato = []
flag = False
for i in range(N) :
    for j in range(M) :
        if board[i][j] == 0 :
            flag = True
        if board[i][j] == 1 :
            tomato.append((i, j))

if flag :
    bfs(tomato)
    print(check() - 1)
else :
    print(0)