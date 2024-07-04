import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs(t) :
    queue = deque()
    for i in t :
        queue.append(i)
    while queue :
        z, x, y = queue.popleft()
        
        for i in range(6) :
            nz = z + dz[i] 
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H :
                if board[nz][nx][ny] == 0 :
                    board[nz][nx][ny] = board[z][x][y] + 1
                    queue.append((nz, nx, ny))

def check() :
    global day
    for i in range(len(board)) :
        for j in range(len(board[i])) :
            for k in range(len(board[i][j])) :
                if board[i][j][k] == 0 :
                    return 0
                day = max(day, board[i][j][k])
    return day

M, N, H = map(int, input().split())
board = []
tomato = []
flag = False
day = 0
for _ in range(H) :
    temp = []
    for _ in range(N) :
        temp.append(list(map(int, input().split())))
    board.append(temp)

for i in range(len(board)) :
    for j in range(len(board[i])) :
        for k in range(len(board[i][j])) :
            if board[i][j][k] == 0 :
                flag = True
            if board[i][j][k] == 1 :
                tomato.append((i, j, k))

if flag : 
    bfs(tomato)
    print(check() - 1)
else :
    print(0)