from collections import deque
def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    queue = deque(people)
    
    t = []
    while queue : 
        if not t :
            t.append(queue.popleft())
        
        if t and queue :
            if t[0] + queue[-1] <= limit :
                t.append(queue.pop())
            
        t = []
        answer += 1
            
        
    return answer