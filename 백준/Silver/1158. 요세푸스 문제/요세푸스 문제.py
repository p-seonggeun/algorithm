from collections import deque
n, k = map(int, input().split())
l = [i + 1 for i in range(n)]
result = []
queue = deque(l)

for i in range(n) :
    queue.rotate(-k + 1)
    result.append(queue.popleft())

print("<", end ="")
print(*result, sep = ", ", end = "")
print(">")