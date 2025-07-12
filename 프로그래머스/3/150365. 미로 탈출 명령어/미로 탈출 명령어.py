import sys
sys.setrecursionlimit(10 ** 6)
def solution(n, m, x, y, r, c, k):
    answer = ''
    x -= 1
    y -= 1
    r -= 1
    c -= 1
    board = [['.' for _ in range(m)] for _ in range(n)]
    board[r][c] = 'E'
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    d = {(-1, 0):'u', (1, 0):'d', (0, -1):'l', (0, 1):'r'}
    
    l = []
    t = []
    
    if abs(abs(x - r) + abs(y - c) - k) % 2 != 0:
        return "impossible"
    
    def dfs(x, y, count):
        if len(t) == 1:
            return
        
        if abs(x - r) + abs(y - c) > k - count:
            return
        
        if x < 0 or x >= n or y < 0 or y >= m :
            return
        
        if board[x][y] == 'E' and (k - count) % 2 != 0:
            return
        
        if count == k:
            if board[x][y] == 'E':
                t.append(''.join(l))
            return
        
        for i in range(4):
            l.append(d[(dx[i], dy[i])])
            x += dx[i]
            y += dy[i]
            
            dfs(x, y, count + 1)
            
            l.pop()
            x -= dx[i]
            y -= dy[i]
            
    dfs(x, y, 0)
    if not t:
        return "impossible"
    return t[0]