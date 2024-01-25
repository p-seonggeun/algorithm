n, m = map(int, input().split())
l = sorted(list(map(int, input().split())))
visited = [False] * 8
p = []

def dfs(index, count) :
    if count == m :
        for i in p :
            if i != 0 :
                print(i, end = " ")
        print()
        return
    
    for i in range(index, n) :
        if not visited[i] :
            p.append(l[i])
            visited[i] = True
            dfs(i, count + 1)
            visited[i] = False
            p.pop()

dfs(0, 0)