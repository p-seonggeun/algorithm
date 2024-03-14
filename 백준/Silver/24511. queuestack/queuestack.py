import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
qs = list(map(int, input().split()))
b = list(map(int, input().split()))
queuestack = deque()
m = int(input())
c = deque(map(int, input().split()))
result = deque()

for i in range(n) :
    if qs[i] == 0 :
        queuestack.appendleft(b[i])

queuestack = queuestack + c

for i in range(m) :
    result.append(queuestack.popleft())
print(*result)
