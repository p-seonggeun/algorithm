import math
N = int(input())
s = set()
for _ in range(N):
    s.add(input().rstrip())

answer = [0, '']
for i in s:
    if i[::-1] in s:
        answer[0] = len(i)
        answer[1] = i[math.floor(len(i) / 2)]

print(*answer)