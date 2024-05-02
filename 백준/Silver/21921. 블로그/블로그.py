import sys
input = sys.stdin.readline

N, X = map(int, input().split())
l = list(map(int, input().split()))
answer = [0, 0]
s = [0] * N
s[0] = l[0]
for i in range(1, N) :
    s[i] = s[i - 1] + l[i]

for i in range(N) :
    if i < X :
        if s[i] > answer[0] :
            answer[0] = s[i]
            answer[1] = 1
        elif s[i] == answer[0] :
            answer[1] += 1
    else :
        if s[i] - s[i - X] > answer[0] :
            answer[0] = s[i] - s[i - X]
            answer[1] = 1
        elif s[i] - s[i - X] == answer[0] :
            answer[1] += 1

if answer[0] == 0 :
    print("SAD")
else :
    print(answer[0])
    print(answer[1])