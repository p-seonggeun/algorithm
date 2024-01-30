import sys
import heapq
input = sys.stdin.readline

n = int(input())
hq = []

for _ in range(n) :
    l = list(map(int, input().split()))
    for i in l :
        heapq.heappush(hq, i)
        if len(hq) > n :
            heapq.heappop(hq)

print(heapq.heappop(hq))