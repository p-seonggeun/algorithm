import sys
input = sys.stdin.readline

N = int(input())
d = {}
for _ in range(N):
    n = int(input())

    if n in d:
        d[n] += 1
    else :
        d[n] = 1

l = []
for i in d :
    l.append([i, d[i]])

l.sort(key = lambda x : (-x[1], x[0]))
print(l[0][0])