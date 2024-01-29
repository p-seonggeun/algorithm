from queue import PriorityQueue
import sys
input = sys.stdin.readline

n = int(input())
queue = PriorityQueue()

for _ in range(n) :
    x = int(input())
    if x == 0 :
        if queue.empty() :
            print(0)
        else :
            print(queue.get()[1])
    else :
        queue.put((-x, x))