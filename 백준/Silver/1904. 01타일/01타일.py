# 1, 00
# 길이 1
# 1
# 길이 2
# 1 + 1, 00
# 길이 3
# 1 + 00, 1 + 1 + 1, 00 + 1
# 길이 4
# 1 + 1 + 00, 00 + 00, 1 + 00 + 1, 1 + 1 + 1 + 1, 00 + 1 + 1

n = int(input())
dp = [0 for _ in range(1000001)]
dp[1] = 1
dp[2] = 2
for i in range(3, n + 1) :
    dp[i] = dp[i - 1] + dp[i - 2]
    if dp[i] >= 15746 :
        dp[i] %= 15746

print(dp[n])