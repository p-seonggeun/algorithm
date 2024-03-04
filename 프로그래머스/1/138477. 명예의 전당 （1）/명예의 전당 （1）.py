import heapq
def solution(k, score):
    answer = []
    temp = []
    for i in score :
        if len(temp) < k :
            heapq.heappush(temp, i)
            
        else :
            t = heapq.heappop(temp)
            if t < i :
                heapq.heappush(temp, i)
            else :
                heapq.heappush(temp, t)
        answer.append(temp[0])
        
            
    
    return answer