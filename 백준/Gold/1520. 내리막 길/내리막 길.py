import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
M, N = map(int, input().split())
board = []
for _ in range(M) :
    board.append(list(map(int, input().split())))

def dfs(x, y) :
    if dp[x][y] == -1 :
        dp[x][y] = 0
        for i in range(4) :
            px = x + dx[i]
            py = y + dy[i]
            if 0 <= px < M and 0 <= py < N :
                if board[px][py] > board[x][y] :
                    dp[x][y] += dfs(px, py)
    return dp[x][y]
dp = [[-1 for _ in range(N)] for _ in range(M)]
dp[0][0] = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(dfs(M - 1, N - 1))