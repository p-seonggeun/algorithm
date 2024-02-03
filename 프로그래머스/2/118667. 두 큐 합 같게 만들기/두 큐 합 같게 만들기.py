from collections import deque
def solution(queue1, queue2):
    count = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum_queue1 = sum(queue1)
    sum_queue2 = sum(queue2)
    max_count = (len(queue1) + len(queue2)) * 2
    
    if (sum_queue1 + sum_queue2) % 2 == 1 :
        return 1
    
    while sum_queue1 != sum_queue2 :
        if count >= max_count :
            return -1
        
        while queue1 and sum_queue1 > sum_queue2 :
            temp = queue1.popleft()
            queue2.append(temp)
            count += 1
            sum_queue1 -= temp
            sum_queue2 += temp
            
        while queue2 and sum_queue2 > sum_queue1 :
                temp = queue2.popleft()
                queue1.append(temp)
                count += 1
                sum_queue2 -= temp
                sum_queue1 += temp
                
    return count