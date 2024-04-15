import sys
input = sys.stdin.readline

n = int(input())
l = sorted(list(map(int, input().split())))
x = int(input())
s, e = 0, n - 1
answer = 0
while s < e :
    if l[s] + l[e] == x :
        answer += 1
        s += 1
        e -= 1
    elif l[s] + l[e] > x :
        e -= 1
    else :
        s += 1

print(answer)