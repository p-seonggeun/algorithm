import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
l = list(map(int, input().split()))

s, e, answer = 0, 0, 0
t = set()
t.add(l[e])
d = {l[e] : 1}
temp = 1
while s <= e and e < N :
    if len(t) <= 2 :
        e += 1
        if e == N :
            answer = max(answer, temp)
            break
        if l[e] in d :
            d[l[e]] += 1
        else : 
            t.add(l[e])
            d[l[e]] = 1
        temp += 1
    else :
        answer = max(answer, temp - 1)    
        if d[l[s]] > 0 : 
            d[l[s]] -= 1
            if d[l[s]] == 0 :
                t.remove(l[s])
                del d[l[s]]
        s += 1
        temp = e - s + 1

print(answer)