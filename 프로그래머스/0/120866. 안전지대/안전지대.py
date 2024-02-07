def solution(board):
    answer = 0
    mine = []
    di = [-1, 0, 1]
    dj = [-1, 0, 1]
    for i in range(len(board)) :
        for j in range(len(board[i])) :
            if board[i][j] == 1 :
                mine.append([i, j])
    
    for i, j in mine :
        for d_i in di :
            for d_j in dj :
                ni = i + d_i
                nj = j + d_j
                
                if ni >= 0 and ni < len(board) and nj >= 0 and nj < len(board) :
                    board[ni][nj] = 1
            
    for i in board :
        print(i)
        answer += i.count(0)
    
    return answer