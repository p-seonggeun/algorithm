n, m = map(int, input().split())
l = sorted(list(map(int, input().split())))
visited = [False] * 8
p = []

def dfs(count) :
    if count == m :
        for i in p :
            print(i, end = " ")
        print()
        return
    
    for i in range(n) :
        if not visited[i] :
            p.append(l[i])
            visited[i] = True

            dfs(count + 1)

            p.pop()
            visited[i] = False

dfs(0)