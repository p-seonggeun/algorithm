import sys

input = sys.stdin.readline
s = list(input().rstrip())
M = int(input())
temp = []

for _ in range(M) :
    c = list(map(str, input().rstrip().split()))
    if c[0] == 'L' :
        if s :
            temp.append(s.pop())
    if c[0] == 'D' :
        if temp :
            s.append(temp.pop())
    if c[0] == 'B' :
        if s :
            s.pop()
    if c[0] == 'P' :
        s.append(c[1])

while temp :
    s.append(temp.pop())

print(''.join(s))