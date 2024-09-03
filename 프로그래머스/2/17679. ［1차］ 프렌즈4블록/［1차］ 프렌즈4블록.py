def dot(m, n, l) :
    c = 0
    for i in range(m) :
        for j in range(n) :
            if l[i][j] == '.' : c += 1
    return c

def down(m, n, l) :
    board = []
    for i in range(n) :
        t = []
        for j in range(m) :
            if l[j][i] == '.' :
                t.insert(0, l[j][i])
            else :
                t.append(l[j][i])
        board.append(t)
    
    for i in range(m) :
        for j in range(n) :
            l[i][j] = board[j][i]

def boom(block, l) :
    while block :
        m, n = block.pop()
        for i in range(m, m + 2) :
            for j in range(n, n + 2) :
                l[i][j] = '.'
                

def check(m, n, board) :
    stand = board[m][n]
    for i in range(m, m + 2) :
        for j in range(n, n + 2) :
            if stand != board[i][j] :
                return []
    return [m, n]

def solution(m, n, board):
    answer = 0
    l = []
    for i in board :
        l.append(list(i))
    flag = True
    while flag : 
        b = []
        for i in range(m - 1) :
            for j in range(n - 1) :
                if l[i][j] != '.' :
                    t = check(i, j, l)
                    if t :
                        b.append(t)
        
        if len(b) == 0 :
            break

        boom(b, l)
        down(m, n, l)
    
    answer = dot(m, n, l)
    return answer