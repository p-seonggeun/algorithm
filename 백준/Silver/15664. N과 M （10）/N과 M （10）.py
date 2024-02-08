n, m = map(int, input().split())
l = sorted(list(map(int, input().split())))
p = []
visited = [False] * n
valid = set()

def dfs(index, count) :
    if count == m :
        temp = []
        for i in p :
            temp.append(str(i))
        temp = tuple(temp)
        if temp not in valid :
            valid.add(temp)
            print(' '.join(temp))
        return
    
    for i in range(index, n) :
        if not visited[i] :
            p.append(l[i])
            visited[i] = True

            dfs(i, count + 1)

            visited[i] = False
            p.pop()

dfs(0, 0)