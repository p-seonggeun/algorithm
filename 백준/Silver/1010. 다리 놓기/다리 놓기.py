import sys
input = sys.stdin.readline

t = int(input())
d = [0] * 31
d[1] = 1
d[2] = 2

for i in range(3, 31) :
    d[i] = d[i - 1] * i

for _ in range(t) :
    n, m = map(int, input().split())
    if n == 0 or m == 0 :
        print(0)
    elif n == m :
        print(1)
    else :
        print(d[m] // (d[m - n] * d[n]))