N = int(input())
l = list(map(int, input()))
goal = list(map(int, input()))

# 0을 누른 경우
lc = l[:]

zero = 1
for i in range(0, 2) :
    if lc[i] == 0 :
        lc[i] = 1
    else :
        lc[i] = 0

for i in range(1, N) :
    if lc[i - 1] != goal[i - 1] : # 다르면 스위치 누름
        if i != N - 1 :
            if lc[i - 1] == 0 :
                lc[i - 1] = 1
            else :
                lc[i - 1] = 0
            if lc[i] == 0 :
                lc[i] = 1
            else :
                lc[i] = 0
            if lc[i + 1] == 0 :
                lc[i + 1] = 1
            else :
                lc[i + 1] = 0
        elif i == N - 1 :
            if lc[i - 1] == 0 :
                lc[i - 1] = 1
            else :
                lc[i - 1] = 0
            if lc[i] == 0 :
                lc[i] = 1
            else :
                lc[i] = 0
        zero += 1
    else :
        continue

answer = 999999
if lc == goal :
    answer = zero

# 0 안누르는 경우
lc = l[:]
one = 0
for i in range(1, N) :
    if lc[i - 1] != goal[i - 1] : # 다르면 스위치 누름
        if i != N - 1 :
            if lc[i - 1] == 0 :
                lc[i - 1] = 1
            else :
                lc[i - 1] = 0
            if lc[i] == 0 :
                lc[i] = 1
            else :
                lc[i] = 0
            if lc[i + 1] == 0 :
                lc[i + 1] = 1
            else :
                lc[i + 1] = 0
        elif i == N - 1 :
            if lc[i - 1] == 0 :
                lc[i - 1] = 1
            else :
                lc[i - 1] = 0
            if lc[i] == 0 :
                lc[i] = 1
            else :
                lc[i] = 0
        one += 1
    else :
        continue

if lc == goal :
    answer = min(answer, one)

if answer == 999999 :
    print(-1)
else :
    print(answer)