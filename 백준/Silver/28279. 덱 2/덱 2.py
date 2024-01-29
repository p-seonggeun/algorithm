from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque()

for _ in range(n) :
    l = input().rstrip().split()
    if len(l) == 1 :
        command = int(l[0])
        if command == 3 :
            if queue :
                print(queue.popleft())
            else :
                print(-1)
        if command == 4 :
            if queue :
                print(queue.pop())
            else :
                print(-1)
        if command == 5 :
            print(len(queue))
        if command == 6 :
            if queue :
                print(0)
            else :
                print(1)
        if command == 7 :
            if queue :
                print(queue[0])
            else :
                print(-1)
        if command == 8 :
            if queue :
                print(queue[-1])
            else :
                print(-1)
    else :
        command = int(l[0])
        num = int(l[1])
        if command == 1 :
            queue.appendleft(num)
        elif command == 2 :
            queue.append(num)