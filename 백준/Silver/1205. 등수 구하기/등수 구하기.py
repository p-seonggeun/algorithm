import sys
input = sys.stdin.readline
N, T, P = map(int, input().split())
if N > 0 :
    scores = list(map(int, input().split()))
else :
    scores = []
flag = False
answer = 0
if scores :
    for index, i in enumerate(scores) :
        if T > i :
            scores.insert(index, T)
            answer = index
            flag = True
            break
    if not flag :
        if len(scores) != P :
            scores.append(T)
            flag = True
else :
    scores.append(T)
    flag = True

if not flag :
    print(-1)
else :
    for i in range(len(scores)) :
        if scores[i] == T :
            print(i + 1)
            break