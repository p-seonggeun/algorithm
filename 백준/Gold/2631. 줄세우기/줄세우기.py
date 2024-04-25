import sys
input = sys.stdin.readline

N = int(input())
l = []
dp = [1] * N
for _ in range(N) :
    l.append(int(input()))

for i in range(N) :
    for j in range(i) :
        if l[j] < l[i] :
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))