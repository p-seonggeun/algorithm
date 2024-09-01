d = {'U' : [-1, 0], 'D' : [1, 0], 'L' : [0, -1], 'R' : [0, 1]}
from collections import deque
def bfs(dirs, s) :
    global answer
    queue = deque()
    queue.append((5, 5))
    
    for i in dirs :
        x, y = queue.popleft()
        
        nx = x + d[i][0]
        ny = y + d[i][1]
        
        if 0 <= nx < 11 and 0 <= ny < 11 :
            if (x, y, nx, ny) not in s :
                s.add((x, y, nx, ny))
                s.add((nx, ny, x, y))
                answer += 1
                queue.append((nx, ny))
            else :
                queue.append((nx, ny))
        else :
            queue.append((x, y))

def solution(dirs):
    global answer
    answer = 0
    board = [[0 for _ in range(11)] for _ in range(11)]
    s = set()
    bfs(dirs, s)
    
    
    return answer