import sys
sys.setrecursionlimit(10 ** 9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
    
def dfs(x, y, r, place, visited) :
    if r == 2 :
        if place[x][y] != 'P' :
            return True

    visited[x][y] = True

    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx <= 4 and 0 <= ny <= 4 :
            if place[nx][ny] == 'O' or place[nx][ny] == 'P' :
                if not visited[nx][ny] :
                    if place[nx][ny] == 'P' :
                        return False
                    else :
                        if not dfs(nx, ny, r + 1, place, visited) :
                            return False
    return True

def check(place, visited) :
    for i in range(5) :
        for j in range(5) :
            r = 0
            if place[i][j] == 'P' :
                if not visited[i][j] :
                    if not dfs(i, j, r, place, visited) :
                        return False
    return True


def solution(places):
    answer = []
    
    for place in places :
        visited = [[False for _ in range(5)] for _ in range(5)]
        if check(place, visited) : 
            answer.append(1)
        else :
            answer.append(0)
            
    return answer