n, m = map(int, input().split())
l = [i for i in range(n + 1)]

for _ in range(m) :
    i, j = map(int, input().split())
    temp = l[i : j + 1]
    temp.reverse()
    l = l[:i] + temp + l[j + 1:]

print(*l[1:])