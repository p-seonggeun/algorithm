N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())
B = []
for _ in range(M):
    B.append(list(map(int, input().split())))

answer = []
for i in range(N): # 3
    t = []
    for j in range(K):
        temp = 0
        for k in range(M):
            temp += A[i][k] * B[k][j]
        t.append(temp)
    answer.append(t)

for i in answer:
    print(*i)