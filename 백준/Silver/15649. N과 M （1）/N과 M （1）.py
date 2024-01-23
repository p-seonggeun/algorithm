n, m = map(int, input().split())
l = [i + 1 for i in range(n)]
visited = [False] * 8
p = []

def dfs(cnt) :
    if cnt == m :
        for i in p :
            print(i, end = " ")
        print()
        return
    
    for i in range(n) :
        if not visited[i] :
            p.append(l[i])
            
            visited[i] = True
            dfs(cnt + 1)

            p.pop()
            visited[i] = False
        
dfs(0)