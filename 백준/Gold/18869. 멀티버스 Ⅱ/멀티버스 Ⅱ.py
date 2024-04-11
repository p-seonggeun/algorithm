import sys
input = sys.stdin.readline

M, N = map(int, input().split())
l = []
for _ in range(M) :
    l.append(list(map(int, input().split())))

temp = []
for i in l : # M
    d = {}
    k = sorted(i)
    for j in range(len(k)) : # N
        d[k[j]] = j

    t = []
    for j in i : # N
        t.append(d[j])
    temp.append(t)

answer = set()
for i in range(M) : # M * M
    for j in range(i + 1, M) :
        if temp[i] == temp[j] : 
            t = tuple(sorted([i, j]))
            if t in answer : continue
            answer.add(t)

print(len(answer))