import sys
from collections import deque
input = sys.stdin.readline

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
            if 0 <= nx < N and 0 <= ny < N :
                if visited[nx][ny] != 99999 :
                    if visited[x][y] + l[nx][ny] < visited[nx][ny] :
                        visited[nx][ny] = visited[x][y] + l[nx][ny]
                        queue.append((nx, ny))
                else :
                    visited[nx][ny] = visited[x][y] + l[nx][ny]
                    queue.append((nx, ny))
    return visited[N - 1][N - 1]
            
answer = 1
while True :
    N = int(input())
    if N == 0 :
        break

    l = [([] * N) for _ in range(N)]
    visited = [[99999] * N for _ in range(N)]
    
    for i in range(N) :
        l[i] = list(map(int, input().split()))
    visited[0][0] = l[0][0]
    print(f"Problem {answer}:", bfs(0, 0))
    answer += 1