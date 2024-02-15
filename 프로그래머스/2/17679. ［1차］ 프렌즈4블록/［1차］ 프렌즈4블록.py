import sys
sys.setrecursionlimit(10 ** 9)
di = [0, 1, 1, 0, 1, -1, -1, -1]
dj = [1, 0, 1, -1, -1, 0, -1, 1]

def dfs(board, target, i, j, m, n, visited) :
    if i < 0 or i >= (m - 1) or j < 0 or j >= (n - 1) :
        return False
    if visited[i][j] :
        return False
    visited[i][j] = True
    
    if board[i][j] == target :
        if (
            target == board[i + di[0]][j + dj[0]] 
                   == board[i + di[1]][j + dj[1]] 
                   == board[i + di[2]][j + dj[2]] 
        ) :
            top = dfs(board, target, i + di[5], j + dj[5], m, n, visited)
            right_top = dfs(board, target, i + di[7], j + dj[7], m, n, visited)
            right = dfs(board, target, i + di[0], j + dj[0], m, n, visited)
            right_down = dfs(board, target, i + di[2], j + dj[2], m, n, visited)
            down = dfs(board, target, i + di[1], j + dj[1], m, n, visited)
            left_down = dfs(board, target, i + di[4], j + dj[4], m, n, visited)
            left = dfs(board, target, i + di[3], j + dj[3], m, n, visited)
            left_top = dfs(board, target, i + di[6], j + dj[6], m, n, visited)
            board[i][j] = '.'
            board[i][j + 1] = '.'
            board[i + 1][j] = '.'
            board[i + 1][j + 1] = '.'
            return True
        return False
    
def solution(m, n, board) :
    answer = 0
    board = [list(i) for i in board]
    count = 0
    
    # print("원본")
    # for i in board :
    #     print(i)
    # print()
    while count != 900 :
        visited = [[False] * n for _ in range(m)]
        count += 1
        for i in range(m - 1) :
            for j in range(n - 1) :
                if board[i][j] == '.' :
                    continue
                # if board[i][j].isalpha() and board[i][j].isupper() and not visited[i][j] :
                target = board[i][j]
                dfs(board, target, i, j, m, n, visited)
        
        # print(count, "번째 지운 후")
        # for i in board :
        #     print(i)
        # print()
        
        temp_board = []
        for i in range(n) :
            temp = []
            for j in range(m) :
                if board[j][i] == '.' :
                    temp.insert(0, board[j][i])
                else :
                    temp.append(board[j][i])
            temp_board.append(temp)
        
        # print(count, "temp_board")
        # for i in temp_board :
        #     print(i)
        # print()
    
        for i in range(m) :
            for j in range(n) :
                board[i][j] = temp_board[j][i]
    
        # print(count, "번째 내린 후")
        # for i in board :
        #     print(i)
        # print()
        
    for i in board :
        answer += i.count('.')
    return answer