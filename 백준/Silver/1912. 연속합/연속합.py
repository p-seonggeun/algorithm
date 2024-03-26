import sys
input = sys.stdin.readline
n = int(input())
l = [0] + list(map(int, input().split()))
d = [-99999] * (n + 1)

for i in range(1, n + 1) :
    d[i] = max(d[i - 1] + l[i], l[i])

print(max(d))