import sys
input = sys.stdin.readline
k, n = map(int, input().split())
l = []
for _ in range(k) :
    l.append(int(input()))

s = 1
e = max(l)

while s < e :
    m = (s + e) // 2 + 1
    cnt = 0
    for i in range(k) :
        cnt += l[i] // m
    if cnt >= n :
        s = m
    else :
        e = m - 1

print(s)