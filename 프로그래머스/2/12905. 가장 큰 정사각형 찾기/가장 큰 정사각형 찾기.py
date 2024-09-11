def solution(board) :
    answer = 0
    r = len(board)
    c = len(board[0])
    
    for i in range(1, r) :
        for j in range(1, c) :
            if board[i][j] == 1 :
                board[i][j] = min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1
    
    for i in board :
        answer = max(answer, max(i))
    
    return answer ** 2