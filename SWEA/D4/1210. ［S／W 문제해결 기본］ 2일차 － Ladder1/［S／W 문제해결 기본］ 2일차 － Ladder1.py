#import sys
from collections import deque
#sys.stdin = open("input.txt", "r")
dx = [0, 0, -1] # 좌, 우, 상
dy = [-1, 1, 0]

def bfs(x, y) :
    queue = deque()
    queue.append((x, y))
    while queue :
        x, y = queue.popleft()
        if x == 0 :
            return y
        for i in range(3) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 100 and 0 <= ny < 100 :
                if board[nx][ny] == 1 :
                    board[nx][ny] += 1
                    queue.append((nx, ny))
                    break


for i in range(1, 11) :
    N = int(input())
    board = []
    for _ in range(100) :
        board.append(list(map(int, input().split())))

    for j in range(100) :
        if board[99][j] == 2 :
            print(f"#{i}", bfs(99, j))
            break

