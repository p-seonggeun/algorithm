n, m = map(int, input().split())
l = [i + 1 for i in range(n)]
visited = [0] * 8


def dfs(index, count) :
    if count == m :
        for i in visited :
            if i :
                print(i, end = " ")
        print()
        return
        
    for i in range(index, n) :
        visited[count] = l[i]
        dfs(i, count + 1)

dfs(0, 0)