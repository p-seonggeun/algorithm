N, K = map(int, input().split())
t = K
flag = True

for i in range(1, N * K):
    if t - 1 < 0:
        flag = False
        break
    t -= 1

if flag:
    if N == 1:
        print(*list(1 for i in range(N * K)))
    else:
        print(*list(i + 1 for i in range(N * K)))
else:
    print(-1)
