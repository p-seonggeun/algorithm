#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
dx = [-1, 0, 1, 1]
dy = [1, 1, 1, 0]

def check() :
    for i in range(N) :
        for j in range(N) :
            for k in range(4) :
                for p in range(5) :
                    nx = i + (dx[k] * p)
                    ny = j + (dy[k] * p)
                    if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 'o':
                        pass
                    else :
                        break
                else :
                    return True
    return False


for tc in range(1, T + 1) :
    N = int(input())
    board = []
    for _ in range(N) :
        board.append(list(input()))
    flag = check()
    if flag :
        print(f"#{tc}", "YES")
    else :
        print(f"#{tc}", "NO")