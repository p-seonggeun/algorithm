#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())

def dfs(n) :
    global answer
    if n == N :
        answer += 1
        return

    for i in range(N) :
        if v1[i] == 0 and v2[n + i] == 0 and v3[n - i] == 0 :
            v1[i] = 1
            v2[n + i] = 1
            v3[n - i] = 1
            dfs(n + 1)
            v1[i] = 0
            v2[n + i] = 0
            v3[n - i] = 0

for tc in range(1, T + 1) :
    N = int(input())
    v1 = [0] * N
    v2 = [0] * (2 * N - 1)
    v3 = [0] * (2 * N - 1)
    answer = 0
    dfs(0)
    print(f"#{tc}", answer)