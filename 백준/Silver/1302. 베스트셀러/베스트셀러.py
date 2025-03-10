N = int(input())

d = {}
for _ in range(N) :
    s = input().rstrip()
    if s in d :
        d[s] += 1
    else :
        d[s] = 1

l = []
for i in d :
    l.append([i, d[i]])

l.sort(key = lambda x : (-x[1], x[0]))
print(l[0][0])