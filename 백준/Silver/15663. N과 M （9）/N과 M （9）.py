n, m = map(int, input().split())
l = sorted(list(map(int, input().split())))
visited = [False] * 8
valid = set()
p = []

def dfs(count) :
    if count == m :
        temp = []
        for i in p :
            temp.append(str(i))
        temp = tuple(temp)
        if temp not in valid :
            valid.add(temp)
            print(' '.join(temp))
        return
    
    for i in range(n) :
        if not visited[i] :
            p.append(l[i])
            visited[i] = True
            dfs(count + 1)
            visited[i] = False
            p.pop()

dfs(0)