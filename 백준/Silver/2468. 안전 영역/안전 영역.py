import copy
from collections import deque

N = int(input())
board = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def gray(l, num) :
    count = 0
    for i in range(N) :
        for j in range(N) :
            if l[i][j] <= num :
                l[i][j] = -1

    for i in range(N) :
        for j in range(N) :
            if l[i][j] != -1 :
                count += 1
                bfs(l, i, j)
    return count

def bfs(l, i, j) :
    queue = deque()
    queue.append((i, j))

    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N :
                if l[nx][ny] != -1 :
                    l[nx][ny] = -1
                    queue.append((nx, ny))

for _ in range(N) :
    board.append(list(map(int, input().split())))

# 최댓값, 최소값 찾기
ma = 0
mi = 0
for i in range(N) :
    for j in range(N) :
        ma = max(board[i][j], ma)
        mi = min(board[i][j], mi)


# 최소값에서 최댓값까지 반복
answer = 0
for i in range(mi, ma + 1) :
    # i보다 작거나 같은 board[i][j]값은 잠김(-1) 처리 하기
    answer = max(gray(copy.deepcopy(board), i), answer)

print(answer)