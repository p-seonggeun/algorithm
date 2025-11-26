N, H, W = map(int, input().split())
board = []

for _ in range(H):
    board.append(list(input()))

answer = []
for i in range(0, N * W, W):
    s = '?'
    for j in range(H):
        for k in range(i, i + W):
            if board[j][k] != '?':
                s = board[j][k]
    answer.append(s)

print(''.join(answer))