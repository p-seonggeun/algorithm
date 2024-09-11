from collections import deque
def bfs(l, visited, n) :
    queue = deque()
    one, two = 0, 0
    for i in range(1, n + 1) :
        if l[i] :
            one = 1
            queue = deque(l[i])
            visited[i] = True
            while queue :
                temp = queue.popleft()
                if not visited[temp] :
                    visited[temp] = True
                    one += 1
                    for j in l[temp] : 
                        queue.append(j)
            
            two = n - one
            return [one, two]
        else :
            one = 1
            two = n - one
            return [one, two]

def solution(n, wires):
    answer = 9999999
    
    for i in range(n - 1) :
        b = [[] for _ in range(n + 1)]
        visited = [False] * (n + 1)
        for index, j in enumerate(wires) :
            if i == index : 
                continue
            b[j[0]].append(j[1])
            b[j[1]].append(j[0])
        
        o, t = 0, 0
        one, two = bfs(b, visited, n)
        answer = min(answer, abs(two - one))
    return answer