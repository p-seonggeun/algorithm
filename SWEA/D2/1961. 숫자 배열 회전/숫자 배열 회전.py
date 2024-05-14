#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1) :
    N = int(input())
    board = []
    for _ in range(N) :
        board.append(list(map(int, input().split())))
    print(f"#{tc}")
    d_9, d_18, d_27 = 0, N - 1, N - 1
    for i in range(N) :
        answer = ''
        for j in range(N - 1, -1, -1) :
            answer += str(board[j][d_9])
        answer += ' '

        for k in range(N - 1, -1, -1) :
            answer += str(board[d_18][k])
        answer += ' '

        for l in range(N) :
            answer += str(board[l][d_27])
        print(answer)

        d_9 += 1
        d_18 -= 1
        d_27 -= 1

