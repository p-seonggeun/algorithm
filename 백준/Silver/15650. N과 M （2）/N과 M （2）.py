n, m = map(int, input().split())
l = [i + 1 for i in range(n)]
visited = [False] * 8

def dfs(index, count) :
    if count == m :
        for i in range(len(visited)) :
            if visited[i] :
                print(l[i], end = " ")
        print()
        return
    
    for i in range(index, n) :
        if not visited[i] :
            visited[i] = True
            dfs(i, count + 1)
            visited[i] = False
        
dfs(0, 0)