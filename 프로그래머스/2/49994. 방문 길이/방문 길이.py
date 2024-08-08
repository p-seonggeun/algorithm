from collections import deque
def solution(dirs):
    answer = 0
    d = { "U" : [-1, 0], "D" : [1, 0], "L" : [0, -1], "R" : [0, 1] }
    board = [[0 for _ in range(11)] for _ in range(11)]
    s = set()
    pos = [5, 5]
    
    for i in dirs :
        
        nx = pos[0] + d[i][0]
        ny = pos[1] + d[i][1]
        
        if 0 <= nx < 11 and 0 <= ny < 11 :
            if (nx, ny, pos[0], pos[1]) and (pos[0], pos[1], nx, ny) not in s :
                answer += 1
                s.add((nx, ny, pos[0], pos[1]))
                s.add((pos[0], pos[1], nx, ny))
            pos[0] = nx
            pos[1] = ny
            board[nx][ny] += 1
            
            
    for i in board :
        print(i)
    return answer