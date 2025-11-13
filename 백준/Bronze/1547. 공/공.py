M = int(input())
l = [1, 2, 3]
for _ in range(M):
    X, Y = map(int, input().split())
    a = l.index(X )
    b = l.index(Y)
    l[a], l[b] = l[b], l[a]

print(l[0])