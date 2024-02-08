n, m = map(int, input().split())
l = sorted(list(map(int, input().split())))
p = []

def dfs(count) :
    if count == m :
        for i in p :
            print(i, end = " ")
        print()
        return 
    
    for i in range(n) :
        p.append(l[i])
        dfs(count + 1)
        p.pop()

dfs(0)