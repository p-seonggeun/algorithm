import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = []
d = [[0] * m for _ in range(n)]
for _ in range(n) :
    l.append(list(map(int, input().split())))

# i, j 방을 방문했을 때 사탕의 최대 개수
# i - 1, j (위쪽)
# i, j - 1 (왼쪽)
# i - 1, j - 1 (대각선)
# 3개 중 최대 + i, j 칸 사탕 개수
# 만약에 인덱스가 벗어날 경우 해당 칸은 0으로 처리

for i in range(n) :
    for j in range(m) :
        if i - 1 < 0 :
            top = 0
        else :
            top = d[i - 1][j]
        if j - 1 < 0 :
            left = 0
        else :
            left = d[i][j - 1]
        if i - 1 < 0 or j - 1 < 0 :
            top_left = 0
        else :
            top_left = d[i - 1][j - 1]
        d[i][j] = max(top, left, top_left) + l[i][j]

print(max(max(d)))