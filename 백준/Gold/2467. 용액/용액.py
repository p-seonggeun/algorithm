import sys
input = sys.stdin.readline
N = int(input())
l = list(map(int, input().split()))

s, e = 0, N - 1
answer = [l[s], l[e]]
m = abs(l[s] + l[e])
flag = True # s를 왼쪽으로
if abs(l[s]) < abs(l[e]) : flag = False # e를 오른쪽으로

while s < e :
    if s >= e or s + 1 == e or e - 1 == s :
        break

    if abs(l[s + 1] + l[e]) < abs(l[s] + l[e - 1]) :
        s += 1
    elif abs(l[s + 1] + l[e]) > abs(l[s] + l[e - 1]) :
        e -= 1
    else :
        if flag : s += 1
        else : e -= 1

    if m >= abs(l[s] + l[e]) :
        m = abs(l[s] + l[e])
        answer = [l[s], l[e]]
        
    # else :
    #     if flag : s += 1
    #     else : e -= 1

answer.sort()
print(*answer)