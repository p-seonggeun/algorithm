import sys
sys.setrecursionlimit(10 ** 6)
def solution(n, lighthouse):
    answer = 0
    visited = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    
    # 내가 켜진 경우와 꺼진 경우
    # 내가 켜진 경우는 자식이 켜져있던 안켜져있던 상관없음
    # 내가 꺼진 경우는 자식이 무조건 켜져있어야함
    # 내가 끝인 경우는 
    
    def dfs(num):
        visited[num] = 1
        on, off = 1, 0
        
        for i in graph[num]:
            if not visited[i]:
                a, b = dfs(i)
                on += min(a, b)
                off += a
        return on, off
        
    for i in lighthouse:
        a, b = i
        graph[a].append(b)
        graph[b].append(a)
    
    on, off = dfs(1)
    answer = min(on, off)
    return answer