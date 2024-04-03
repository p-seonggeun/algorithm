import sys
input = sys.stdin.readline
N, D = map(int, input().split())
shortcut = []
dp = [0] * (D + 1)

for i in range(D + 1) :
    dp[i] = i

for _ in range(N) :
    s, e, distance = map(int, input().split())
    if e > D :
        continue
    if e - s < distance :
        continue

    shortcut.append([s, e, distance])

shortcut.sort(key = lambda x : x[0])

for i in shortcut :
    dp[i[1]] = min(dp[i[1]], dp[i[0]] + i[2])
    for j in range(D + 1) :
        dp[j] = min(dp[j - 1] + 1, dp[j])

print(dp[D])