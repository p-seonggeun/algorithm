import sys
input = sys.stdin.readline
t = int(input())

d = [0] * 191230
d[1] = 1
d[2] = 2

for i in range(3, 191230) :
    d[i] = (d[i - 1] + d[i - 2]) % (10 ** 9 + 7)

for _ in range(t) :
    n = int(input())
    print(d[n])