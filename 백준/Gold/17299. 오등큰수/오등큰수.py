import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
d = {}
stack = []
answer = [-1] * n

for i in l :
    if i in d :
        d[i] += 1
    else :
        d[i] = 1

for i in range(n) :
    while stack != [] and d[stack[-1][1]] < d[l[i]] :
        answer[stack.pop()[0]] = l[i]
    stack.append([i, l[i]])

print(*answer)