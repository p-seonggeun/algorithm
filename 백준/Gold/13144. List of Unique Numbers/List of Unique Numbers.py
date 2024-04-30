import sys
input = sys.stdin.readline
N = int(input())
l = list(map(int, input().split()))
d = {}
s, e = 0, 0
d[l[s]] = s
answer = 1
while s <= e :
    if e == N - 1 : 
        break
    e += 1
    if l[e] in d :
        delete = []
        for key, value in d.items() :
            if value < d[l[e]] :
                delete.append(key)
        for i in delete :
            del d[i]
        s = d[l[e]] + 1
        answer += e - s + 1
        d[l[e]] = e
    else :
        answer += e - s + 1
        d[l[e]] = e

print(answer)