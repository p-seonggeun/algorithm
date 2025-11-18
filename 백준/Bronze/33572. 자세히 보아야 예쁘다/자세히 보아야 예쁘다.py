import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))

heapq.heapify(A)

while A and M > 0:
    time = heapq.heappop(A)
    M -= (time - 1)

if M > 0:
    print("OUT")
else:
    print("DIMI")
