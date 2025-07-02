N = int(input())
dp = [[0, 0] for _ in range(101)]
dp[0] = [1, 1]
dp[1] = [2, 1]

for i in range(2, 101):
    r = dp[i - 1][0]
    c = dp[i - 1][1]

    if (r + 1) * c >= r * (c + 1):
        dp[i][0] = r + 1
        dp[i][1] = c
    else:
        dp[i][0] = r
        dp[i][1] = c + 1

print(dp[N][0] * dp[N][1])