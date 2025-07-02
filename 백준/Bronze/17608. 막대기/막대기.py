import sys
input = sys.stdin.readline

N = int(input())
l = []
for _ in range(N):
    l.append(int(input()))

answer = 0
s = 0
for i in range(N - 1, -1, -1):
    if s < l[i]:
        s = l[i]
        answer += 1
print(answer)