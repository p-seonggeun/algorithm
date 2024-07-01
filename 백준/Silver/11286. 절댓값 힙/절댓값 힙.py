import sys
import heapq
input = sys.stdin.readline

l = []
N = int(input())
for _ in range(N) :
    x = int(input())
    if x == 0 :
        if len(l) >= 2 :
            temp = heapq.heappop(l)
            temp2 = heapq.heappop(l)
            if temp[0] == temp2[0] :
                if temp[1] < temp2[1] :
                    heapq.heappush(l, temp2)
                    print(temp[1])
                else :
                    heapq.heappush(l, temp)
                    print(temp2[1])
            else :
                heapq.heappush(l, temp2)
                print(temp[1])
        elif len(l) == 1 :
            print(heapq.heappop(l)[1])
        else :
            print(0)
    else :
        heapq.heappush(l, (abs(x), x))