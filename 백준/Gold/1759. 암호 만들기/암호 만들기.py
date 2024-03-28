L, C = map(int, input().split(" "))
l = sorted(input().rstrip().split(" "))
stack = []
visited = [False] * C
def dfs(index, count) :
    if count == L :
        a, b = 0, 0
        for i in stack :
            if i in ['a', 'e', 'i', 'o', 'u'] :
                a += 1
            else :
                b += 1
        if a >= 1 and b >= 2 :
            print(''.join(stack))
            return
    for i in range(index, C) :
        if visited[i] == False :
            visited[i] = True
            stack.append(l[i])
            dfs(i, count + 1)
            stack.pop()
            visited[i] = False
dfs(0, 0)