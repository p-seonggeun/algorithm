from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque()
for _ in range(n) :
    l = input().rstrip().split()
    if len(l) == 1 :
        command = l[0]
        if command == 'pop' :
            if queue :
                print(queue.popleft())
            else :
                print(-1)
        elif command == 'size' :
            print(len(queue))
        elif command == 'empty' :
            if queue :
                print(0)
            else :
                print(1)
        elif command == 'front' :
            if queue :
                print(queue[0])
            else :
                print(-1)
        elif command == 'back' :
            if queue :
                print(queue[-1])
            else :
                print(-1)
    else :
        command = l[0]
        num = int(l[1])
        queue.append(num)