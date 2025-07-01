board = [[0 for _ in range(100)] for _ in range(100)]

for i in range(4):
    sx, sy, ex, ey = map(int, input().split())

    for j in range(sx, ex) :
        for k in range(sy, ey):
            board[j][k] = 1

answer = 0
for i in board:
    answer += sum(i)
print(answer)