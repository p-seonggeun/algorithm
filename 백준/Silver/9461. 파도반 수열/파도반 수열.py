import sys
input = sys.stdin.readline

t = int(input())
d = [0] * 101
d[0] = 0
d[1] = 1
d[2] = 1
d[3] = 1
for i in range(4, 101) :
    d[i] = d[i - 2] + d[i - 3]
for _ in range(t) :
    n = int(input())
    print(d[n])