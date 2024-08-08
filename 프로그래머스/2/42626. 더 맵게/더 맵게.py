from heapq import *
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while scoville[0] < K :
        if not scoville :
            return -1
        try :
            f = heappop(scoville)
            s = heappop(scoville)
        except:
            return -1
        
        heappush(scoville, f + 2 * s)
        answer += 1
    return answer