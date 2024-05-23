dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

def dfs(x, y, z) :
    if x <= 0 or y <= 0 or z <= 0 :
        return 1
    if x > 20 or y > 20 or z > 20 :
        return dfs(20, 20, 20)

    if dp[x][y][z] != 0 :
        return dp[x][y][z]

    if x < y and y < z :
        dp[x][y][z] = dfs(x, y, z - 1) + dfs(x, y - 1, z - 1) - dfs(x, y - 1, z)
    else :
        dp[x][y][z] = dfs(x - 1, y, z) + dfs(x - 1, y - 1, z) + dfs(x - 1, y, z - 1) - dfs(x - 1, y - 1, z - 1)

    return dp[x][y][z]

import sys
input = sys.stdin.readline
while True :
    a, b, c = map(int, input().split())
    if a == b == c == -1 :
        break
    print(f"w({a}, {b}, {c}) =", dfs(a, b, c))