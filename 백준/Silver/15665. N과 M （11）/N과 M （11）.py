n, m = map(int, input().split())
l = sorted(list(map(int, input().split())))
stack = []
s = set()

def dfs(count) :
    if count == m :
        if ''.join(stack) not in s :
            s.add(''.join(stack))
            print(' '.join(stack))
        return
    for i in range(n) :
        stack.append(str(l[i]))
        dfs(count + 1)
        stack.pop()

dfs(0)