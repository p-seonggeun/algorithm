import sys
input = sys.stdin.readline

N, K = map(int, input().split())
data = [(0, 0)]
for _ in range(N):
    W, V = map(int, input().split())
    data.append((W, V))

dp = [[0] * (K + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
    for j in range(K + 1):
        if j >= data[i][0]:
            dp[i][j] = dp[i - 1][j - data[i][0]] + data[i][1]
        dp[i][j] = max(dp[i][j], dp[i - 1][j])

print(max(dp[N]))