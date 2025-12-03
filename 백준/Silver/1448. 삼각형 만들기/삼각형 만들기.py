import sys
input = sys.stdin.readline

N = int(input())
l = []
for _ in range(N):
    l.append(int(input()))

l.sort(reverse=True)
for i in range(len(l) - 2):
    if l[i] < l[i + 1] + l[i + 2]:
        print(l[i] + l[i + 1] + l[i + 2])
        break
else:
    print(-1)