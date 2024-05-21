def check_row(r, i) :
    for j in range(9) :
        if board[r][j] == i :
            return False
    return True

def check_col(c, i) :
    for j in range(9) :
        if board[j][c] == i :
            return False
    return True

def check_box(r, c, i) :
    for j in range(3) :
        for k in range(3) :
            if board[(r // 3) * 3 + j][(c // 3) * 3 + k] == i :
                return False
    return True

def check(n) :
    if n == len(zero) :
        for i in board :
            print(*i)
        exit()

    for i in range(1, 10) :
        row = zero[n][0]
        col = zero[n][1]
        if check_row(row, i) and check_col(col, i) and check_box(row, col, i) :
            board[row][col] = i
            check(n + 1)
            board[row][col] = 0
import sys
input = sys.stdin.readline
board = []
diff = [i + 1 for i in range(9)]
for _ in range(9) :
    board.append(list(map(int, input().split())))

zero = []
for i in range(9) :
    for j in range(9) :
        if board[i][j] == 0 :
            zero.append([i, j])
check(0)