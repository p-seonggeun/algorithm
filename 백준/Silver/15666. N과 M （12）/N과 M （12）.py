n, m = map(int, input().split())
l = sorted(list(map(int, input().split())))
valid = set()
p = [0] * 8

def dfs(index, count) :
    if count == m :
        temp = []
        for i in p :
            if i :
                temp.append(str(i))
        temp = tuple(temp)
        if temp not in valid :
            valid.add(temp)
            print(' '.join(temp))
        return
    
    for i in range(index, n) :
        p[count] = l[i]
        dfs(i, count + 1)
    

dfs(0, 0)