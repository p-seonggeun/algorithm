import sys
input = sys.stdin.readline

N = int(input())
board = []
white, blue = 0, 0

def dfs(n, r, c) :
    global white, blue

    s = board[r][c]
    if n == 1 : 
        if s == 1 : blue += 1
        else : white += 1
        return
    
    half = n // 2

    for i in range(r, r + n) :
        for j in range(c, c + n) :
            if board[i][j] != s : # 전체 종이에 다른색이 있을 경우
                dfs(half, r, c) # 1
                dfs(half, r, c + half) # 2
                dfs(half, r + half, c) # 3
                dfs(half, r + half, c + half) # 4
                return
            
    if s == 1 : blue += 1 
    else : white += 1 
    return

for _ in range(N) :
    board.append(list(map(int, input().split())))

dfs(N, 0, 0)
print(white)
print(blue)