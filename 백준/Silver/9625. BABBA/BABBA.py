# A -> B
# B -> BA

# A
# B
# BA
# BAB
# BABBA
# BABBABAB
# BABBABABBABBA
# BABBABABBABBABABBABAB

K = int(input())
dp = [[0, 0] for _ in range(46)]
dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, 46):
    dp[i][0] = dp[i - 2][0] + dp[i - 1][0]
    dp[i][1] = dp[i - 2][1] + dp[i - 1][1]

print(*dp[K])