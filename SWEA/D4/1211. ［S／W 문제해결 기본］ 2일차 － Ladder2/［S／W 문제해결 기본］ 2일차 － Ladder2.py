#import sys
from collections import deque

#sys.stdin = open("input.txt", "r")
dx = [0, 0, -1]  # 좌, 우, 상
dy = [-1, 1, 0]


def bfs(x, y, length, copy_board):
    queue = deque()
    queue.append((x, y, length))
    while queue:
        x, y, length = queue.popleft()
        if x == 0:
            return [y, length]
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 100 and 0 <= ny < 100:
                if copy_board[nx][ny] == 1:
                    copy_board[nx][ny] += 1
                    queue.append((nx, ny, length + 1))
                    break


for i in range(1, 11):
    N = int(input())
    board = []
    for _ in range(100):
        board.append(list(map(int, input().split())))
    standard = 1e9
    answer = -1
    for j in range(100):
        if board[99][j] == 0:
            continue
        copy = [item[:] for item in board]
        temp = bfs(99, j, 0, copy)
        if temp[1] < standard:
            standard = temp[1]
            answer = temp[0]
        elif temp[1] == standard:
            if answer < temp[0]:
                answer = temp[0]

    print(f"#{i}", answer)
