import heapq
def solution(scoville, K):
    answer = 0
    
    h = []
    for i in scoville:
        heapq.heappush(h, i)
        
    while len(h) >= 2 and h[0] < K:
        a = heapq.heappop(h)
        b = heapq.heappop(h)
        c = a + (2 * b)
        
        heapq.heappush(h, c)
        answer += 1
    
    if h[0] < K:
        return -1
    return answer