from collections import deque
n = int(input())
queue = deque(enumerate(map(int, input().split())))
answer = []

while queue :
    a, b = queue.popleft()
    answer.append(a + 1)

    if b > 0 :
        queue.rotate(-(b - 1))
    else :
        queue.rotate(-b)

print(' '.join(map(str, answer)))