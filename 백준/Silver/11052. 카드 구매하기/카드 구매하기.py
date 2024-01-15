n = int(input())
l = list(map(int, input().split()))
l.insert(0, 0)
d = [0] * (len(l))

for i in range(1, n + 1) :
    for j in range(1, i + 1) :
        d[i] = max(d[i - j] + l[j], d[i])

print(d[n])