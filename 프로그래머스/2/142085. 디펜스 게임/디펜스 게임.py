import heapq
def solution(n, k, enemy):
    answer = 0
    queue = []
    
    for index, i in enumerate(enemy) :
        n -= i
        heapq.heappush(queue, -i)
        
        if n < 0 :
            if k > 0 :
                n += -heapq.heappop(queue)
                k -= 1
                answer += 1
            else :
                answer = index
                break
        else :
            answer += 1
    return answer