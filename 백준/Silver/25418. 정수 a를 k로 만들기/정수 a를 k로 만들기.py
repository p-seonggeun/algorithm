A, K = map(int, input().split())

dp = [1e9] * (K + 1)
dp[A] = 0

for i in range(A + 1, K + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[K])
