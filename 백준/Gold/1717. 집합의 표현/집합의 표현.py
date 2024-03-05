def find(x) :
    if s[x] == x :
        return x
    else :
        s[x] = find(s[x])
        return s[x]

def merge(a, b) :
    a = find(a)
    b = find(b)
    if a == b :
        return
    s[b] = a

def isUnion(a, b) :
    a = find(a)
    b = find(b)
    if a == b :
        return True
    else :
        return False

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

s = []

for i in range(n + 1) :
    s.append(i)
    
for _ in range(m) :
    o, a, b = map(int, input().split())
    if o == 0 :
        merge(a, b)
    else :
        if isUnion(a, b) :
            print("YES")
        else :
            print("NO")