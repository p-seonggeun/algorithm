import sys
input = sys.stdin.readline
bingo = [
    [0, 1, 2],
    [0, 3, 6],
    [0, 4, 8],
    [1, 4, 7],
    [2, 4, 6],
    [2, 5, 8],
    [3, 4, 5],
    [6, 7, 8]
]

def check(board) :
    x = board.count('X')
    o = board.count('O')

    l = []
    for i in bingo :
        a, b, c = i
        if board[a] == board[b] == board[c] and board[a] != '.' :
            l.append(board[a])
    
    if len(set(l)) == 1 :
        if l[0] == 'X' :
            if x == o + 1 :
                return True
        else :
            if x == o :
                return True
    elif len(set(l)) == 0 :
        if x == 5 and o == 4 :
            return True
    
    return False

while True :
    s = input().rstrip()
    if s == 'end' :
        break

    if check(s) :
        print("valid")
    else :
        print("invalid")