import sys
input = sys.stdin.readline
N = int(input())
l = []

for _ in range(N):
    l.append(int(input()))

l.sort(reverse=True)
for i in l:
    print(i)