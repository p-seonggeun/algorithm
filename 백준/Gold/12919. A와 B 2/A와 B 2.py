import sys
input = sys.stdin.readline

def dfs(t) :
    global flag

    if len(t) == len(S) :
        if t == S :
            flag = True
        return
    
    if t[0] == 'B' :
        t.reverse()
        t.pop()
        dfs(t)
        t.append('B')
        t.reverse()

    if t[-1] == 'A' :
        t.pop()
        dfs(t)
        t.append('A')

S = list(map(str, input().rstrip()))
T = list(map(str, input().rstrip()))
flag = False

dfs(T)
if flag :
    print(1)
else :
    print(0)