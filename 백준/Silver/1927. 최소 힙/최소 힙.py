from queue import PriorityQueue
import sys
input = sys.stdin.readline
queue = PriorityQueue()

n = int(input())

for _ in range(n) :
    x = int(input())
    if x == 0 :
        if queue.empty() :
            print(0)
        else :
            print(queue.get())
    else :
        queue.put(x)