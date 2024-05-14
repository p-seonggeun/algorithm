#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())

def check_row(x) :
    checked_row = [False] + [True] * 9
    for i in range(9) :
        if checked_row[board[x][i]] == False :
            return False
        else :
            checked_row[board[x][i]] = False
    if True in checked_row :
        return False
    return True

def check_col(y) :
    checked_col = [False] + [True] * 9
    for i in range(9) :
        if checked_col[board[i][y]] == False :
            return False
        else :
            checked_col[board[i][y]] = False
    if True in checked_col :
        return False
    return True

def check_block(x, y) :
    checked_block = [False] + [True] * 9
    for i in range(3) :
        for j in range(3) :
            if checked_block[board[x + i][y + j]] == False :
                return False
            else :
                checked_block[board[x + i][y + j]] = False
    if True in checked_block :
        return False
    return True

def check() :
    for i in range(9) :
        if not (check_row(i) and check_col(i)) :
            return False

    l = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]

    for i in l :
        x, y = i
        if not check_block(x, y) :
            return False

    return True

for tc in range(1, T + 1) :
    board = []
    for _ in range(9) :
        board.append(list(map(int, input().split())))

    if check() :
        answer = 1
    else : answer = 0


    print(f"#{tc}", answer)
