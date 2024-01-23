n, m = map(int, input().split())
p = []

def dfs(cnt) :
    if cnt == m :
        for i in p :
            print(i, end = " ")
        print()
        return
    
    for i in range(1, n + 1) :
        p.append(i)
        dfs(cnt + 1)
        p.pop()

dfs(0)