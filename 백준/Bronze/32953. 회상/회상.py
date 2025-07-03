N, M = map(int, input().split())
d = {}
for _ in range(N):
    K = int(input())
    student = list(map(int, input().split()))
    for i in student:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

answer = 0
for i in d.values():
    if i >= M:
        answer += 1
print(answer)