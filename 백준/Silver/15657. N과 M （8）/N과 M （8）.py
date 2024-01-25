n, m = map(int, input().split())
l = sorted(list(map(int, input().split())))

p = [0] * 8

def dfs(index, count) :
    if count == m :
        for i in p :
            if i != 0 :
                print(i, end = " ")
        print()
        return
    
    for i in range(index, n) :
        p[count] = l[i]
        dfs(i, count + 1)

dfs(0, 0)