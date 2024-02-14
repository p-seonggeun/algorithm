n = int(input())
l = []
m = []
for _ in range(n) :
    x, y = map(int, input().split())
    l.append(x)
    m.append(y)

print(abs(max(l) - min(l)) * abs(max(m) - min(m)))