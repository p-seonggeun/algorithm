import sys
input = sys.stdin.readline

N, S = map(int, input().split())
l = []
for _ in range(N):
    t = int(input())
    if t < S:
        l.append(t)
l.sort()

left, right = 0, len(l) - 1
answer = 0
while left < right:
    if l[left] + l[right] <= S:
        answer += right - left
        left += 1
    else:
        right -= 1

print(answer)