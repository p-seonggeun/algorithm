import sys
input = sys.stdin.readline

T = int(input())
ex = [0, 0]
answer = 0
for i in range(1, T + 1):
    l, r = map(int, input().split())

    if i >= 2:
        if l != 0:
            if l == ex[0]:
                answer += 1
        if r != 0:
            if r == ex[1]:
                answer += 1

    if l != 0 and r != 0:
        if l == r:
            answer += 1

    ex[0] = l
    ex[1] = r

print(answer)