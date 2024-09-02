import heapq
def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while True :
        try :
            a = heapq.heappop(scoville)
            if a >= K :
                break
            b = heapq.heappop(scoville)
        except :
            return -1
        
    
        c = a + (b * 2)
        heapq.heappush(scoville, c)
        answer += 1
    
    return answer