from collections import deque
def solution(priorities, location):
    answer = 0
    
    a = sorted(priorities)
    
    l = deque()
    for index, i in enumerate(priorities):
        l.append([index, i])
    
    m = a.pop()
    while m and l:
        t = l.popleft()
        
        if m <= t[1]:
            answer += 1
            if location == t[0]:
                return answer
            m = a.pop()
        else:
            l.append(t)
            
    return answer