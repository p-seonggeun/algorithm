from collections import deque
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
R, C = map(int, input().split())
board = []
visited = [[[False, False] for _ in range(C)] for _ in range(R)]

for _ in range(R) :
    board.append(list(input().rstrip()))

fire = []
J = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
d = {}

for i in range(len(board)) :
    for j in range(len(board[i])) :
        if board[i][j] == 'J' :
            J = (i, j, 'J', 0)
            if i == 0 or i == R - 1 or j == 0 or j == C - 1 :
                print(1)
                exit(0)
        if board[i][j] == 'F' :
            d['F' + str(len(fire))] = (i, j)
            fire.append((i, j, 'F' + str(len(fire)), 0))

escape_j = {}
escape_fire = {}

def bfs(j, f) :
    queue = deque()
    queue.append(j)
    for i in f :
        queue.append(i)
    
    while queue :
        x, y, who, time = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < R and 0 <= ny < C) :
                if board[nx][ny] == '#' :
                    continue
                if board[nx][ny] == '.' :
                    if who == 'J' :
                        if not visited[nx][ny][0] :
                            visited[nx][ny][0] = True
                            queue.append((nx, ny, who, time + 1))
                    elif 'F' in who :
                        if not visited[nx][ny][1] :
                            visited[nx][ny][1] = True
                            queue.append((nx, ny, who, time + 1))

                    if nx == 0 or nx == R - 1 or ny == 0 or ny == C - 1 :
                        if who == 'J' :
                            if (nx, ny) not in escape_j :
                                escape_j[(nx, ny)] = [abs(J[0] - nx) + abs(J[1] - ny), time + 1]
                            # escape_j.add(((nx, ny), abs(J[0] - nx) + abs(J[1] - ny), time))
                        else :
                            if (nx, ny) not in escape_fire :
                                escape_fire[(nx, ny)] = [abs(d[who][0] - nx) + abs(d[who][1] - ny), time + 1]
                            # escape_fire.add(((nx, ny), abs(d[who][0] - nx) + abs(d[who][1] - ny), time))

bfs(J, fire)

s_escape_j = sorted(escape_j.items(), key = lambda x : max(x[1]))
s_escape_fire = sorted(escape_fire.items(), key = lambda x : max(x[1]))

answer = [[0, 0], 999999]
flag = True
if escape_fire :
    for i in s_escape_j :
        if flag :
            for j in s_escape_fire :
                if i[0] == j[0] :
                    if max(i[1]) < max(j[1]) :
                        if max(i[1]) < answer[1] :
                            answer = [i[0], max(i[1])]
                            flag = False
                            break
else :
    if escape_j :
        answer = [s_escape_j[0][0], max(s_escape_j[0][1])]
    else :
        answer = "IMPOSSIBLE"

if answer == 'IMPOSSIBLE' or answer == [[0, 0], 999999] :
    print("IMPOSSIBLE")
else :
    print(answer[1] + 1)