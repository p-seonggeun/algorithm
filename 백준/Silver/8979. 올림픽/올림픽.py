import sys
input = sys.stdin.readline

N, K = map(int, input().split())

score = {}

for _ in range(N) :
    temp = list(map(int, input().split()))
    n, s = temp[0], tuple(temp[1:])
    if s in score :
        score[s].append(n)
    else :
        score[s] = [n]

temp = list(score.items())
temp.sort(key = lambda x : (-x[0][0], -x[0][1], -x[0][2]))
answer = 0
for index, i in enumerate(temp) :
    if K in i[1] :
        answer += 1
        break
    else :
        answer += len(i[1])

print(answer)