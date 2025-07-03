r, c = map(int, input().split())
T = int(input())
R = [0, r]
C = [0, c]
for _ in range(T):
    a, b = map(int, input().split())
    if a == 1:
        R.append(b)
    else:
        C.append(b)

R.sort()
C.sort()

A = []
for i in range(len(R) - 1):
    A.append(R[i + 1] - R[i])
B = []
for i in range(len(C) - 1):
    B.append(C[i + 1] - C[i])

answer = 0
for i in A:
    for j in B:
        answer = max(answer, i * j)
print(answer)