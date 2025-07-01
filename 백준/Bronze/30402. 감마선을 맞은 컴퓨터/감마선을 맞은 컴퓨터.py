board = []
for _ in range(15):
    board.append(input().split())

for i in range(15):
    for j in range(15):
        if board[i][j] == 'w':
            print("chunbae")
            exit(0)
        elif board[i][j] == 'b':
            print("nabi")
            exit(0)
        elif board[i][j] == 'g':
            print("yeongcheol")
            exit(0)
