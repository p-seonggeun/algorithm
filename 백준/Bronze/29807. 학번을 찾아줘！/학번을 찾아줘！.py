T = int(input())
l = list(map(int, input().split()))
while len(l) != 5:
    l.append(0)
answer = 0

if l[0] > l[2]:
    answer += abs(l[0] - l[2]) * 508
else:
    answer += abs(l[0] - l[2]) * 108

if l[1] > l[3]:
    answer += abs(l[1] - l[3]) * 212
else:
    answer += abs(l[1] - l[3]) * 305

if T == 5:
    answer += l[4] * 707

answer *= 4763
print(answer)
