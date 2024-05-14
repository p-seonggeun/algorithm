#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1) :
    N = int(input())
    board = []
    for _ in range(N) :
        board.append(list(map(int, input())))

    row = 0
    col = (N - 1) // 2 # 열 시작점
    count = 1
    step = 2
    answer = 0
    while row < N :
        for i in range(col, col + count) :
            answer += board[row][i]

        if row >= (N - 1) // 2 :
            step = -2
            col += 1
        else :
            col -= 1
            step = 2

        count += step
        row += 1

    print(f"#{tc}", answer)
