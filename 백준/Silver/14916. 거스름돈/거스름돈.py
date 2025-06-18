n = int(input())
INF = 1e9
dp = [INF] * 100001
dp[2] = 1
dp[5] = 1

for i in range(3, 100001) :
    if i % 5 == 0 :
        dp[i] = min(dp[i], dp[i - 5] + 1)
    elif i % 2 == 0 :
        dp[i] = min(dp[i], dp[i - 2] + 1)
    else :
        dp[i] = min(dp[i], dp[i - 2] + 1, dp[i - 5] + 1)

if dp[n] == INF :
    print(-1)
else :
    print(dp[n])