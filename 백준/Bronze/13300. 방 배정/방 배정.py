import math
N, K = map(int, input().split())
d = {}

for _ in range(N) :
    S, Y = map(str, input().split())
    if S + Y in d :
        d[S + Y].append(1)
    else :
        d[S + Y] = [1]

answer = 0
for i in d:
    answer += math.ceil(len(d[i]) / K)
print(answer)