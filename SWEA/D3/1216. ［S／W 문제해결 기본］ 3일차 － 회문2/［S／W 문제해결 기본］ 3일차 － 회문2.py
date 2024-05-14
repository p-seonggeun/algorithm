#import sys
#sys.stdin = open("input.txt", "r")

T = 10

def check(arr, leng) :
    for a in arr :
        for i in range(N - leng + 1) :
            temp = a[i : i + leng]
            for j in range(leng // 2) :
                if temp[j] != temp[leng - 1 - j] :
                    break
            else :
                return True
    return False

for t in range(10) :
    tc = int(input())
    N = 100
    board = []
    for _ in range(100) :
        board.append(list(input()))
    board2 = [''.join(i) for i in (zip(*board))]
    answer = 0

    for l in range(N, 0, -1) :
        if check(board, l) or check(board2, l) :
            break

    print(f"#{tc}", l)