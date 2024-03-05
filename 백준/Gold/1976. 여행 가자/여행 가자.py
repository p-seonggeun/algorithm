def find(x) :
    if group[x] == x :
        return x
    else :
        group[x] = find(group[x])
        return group[x]

def merge(a, b) :
    a = find(a)
    b = find(b)
    if a > b :
        group[a] = b
    else :
        group[b] = a

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n)]
group = [i for i in range(n)]

for i in range(n) :
    l = list(map(int, input().split()))
    for index, j in enumerate(l) :
        if j == 1 :
            graph[i].append(index)

for index, i in enumerate(graph) :
    for j in i :
        merge(index, j)

result = set()
visit = list(map(int, input().split()))
for i in visit :
    result.add(group[i - 1])

if len(result) == 1 :
    print("YES")
else :
    print("NO")