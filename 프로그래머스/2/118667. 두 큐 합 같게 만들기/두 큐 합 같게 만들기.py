from collections import deque
def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    count = (len(queue1) + len(queue2)) * 2 
    s_q1 = sum(queue1)
    s_q2 = sum(queue2)
    
    
    while queue1 and queue2 and s_q1 != s_q2 :
        if answer >= count : return -1
        while queue1 and s_q1 > s_q2 :
            t = queue1.popleft()
            s_q1 -= t
            s_q2 += t
            queue2.append(t)
            answer += 1
        
        while queue2 and s_q1 < s_q2 :
            t = queue2.popleft()
            s_q2 -= t
            s_q1 += t
            answer += 1
            queue1.append(t)
    
    if queue1 and queue2 :
        return answer
    else :
        return -1