N = int(input())
L = [0] + list(map(int, input().split()))
J = [0] + list(map(int, input().split()))

dp = [[-999] * 100 for _ in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
    for j in range(100):
        if j >= L[i]:
            dp[i][j] = dp[i - 1][j - L[i]] + J[i]
        dp[i][j] = max(dp[i][j], dp[i - 1][j])

print(max(dp[N]))