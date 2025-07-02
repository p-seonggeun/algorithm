import sys
input = sys.stdin.readline

N = int(input())
d = {}
for _ in range(N):
    S, X = map(str, input().split(" "))
    X = int(X)

    if S in d:
        d[S] += X
    else:
        d[S] = X

flag = False
for i in d:
    if d[i] == 5:
        flag = True
        break

if flag:
    print("YES")
else:
    print("NO")