from collections import deque
A, B = map(int, input().split())

def bfs(start):
    queue = deque()
    queue.append(start)

    while queue:
        now, count = queue.popleft()

        if now == B:
            return count

        if now > B:
            continue

        queue.append((now * 2, count + 1))
        queue.append((int(str(now) + '1'), count + 1))

answer = bfs((A, 0))
if answer == None:
    print(-1)
else:
    print(answer + 1)