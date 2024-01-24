import sys
input = sys.stdin.readline

m = int(input())
s = set()

for _ in range(m) :
    l = list(input().rstrip().split())
    if len(l) == 2 :
        mode = l[0]
        x = int(l[1])
    else :
        mode = l[0]
        
    if mode == 'add' :
        if x not in s :
            s.add(x)
    elif mode == 'remove' :
        if x in s :
            s.remove(x)
    elif mode == 'check' :
        if x in s :
            print(1)
        else :
            print(0)
    elif mode == 'toggle' :
        if x in s :
            s.remove(x)
        else :
            s.add(x)
    elif mode == 'all' :
        s = set([i for i in range(1, 21)])
    elif mode == 'empty' :
        s = set()