import sys, time
from collections import deque
input = sys.stdin.readline

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

def bfs(i, j) :
    queue = deque()
    board[i][j] = 1
    queue.append((i, j))
    while queue :
        x, y = queue.popleft()
        for i in range(8) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < l and 0 <= ny < l :
                if board[nx][ny] == 'E' :
                    return board[x][y]
                if board[nx][ny] == 0 :
                    board[nx][ny] = board[x][y] + 1
                    queue.append((nx, ny))

                    

T = int(input())
for _ in range(T) :
    l = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    if sx == ex and sy == ey :
        print(0)
        continue
    board = [[0 for _ in range(l)] for _ in range(l)]
    
    board[ex][ey] = 'E'
    print(bfs(sx, sy))
    