from collections import deque
def solution(priorities, location):
    answer = 0
    prior = deque()
    for index, i in enumerate(priorities) :
        prior.append([index, i])
    
    while prior :
        now = prior.popleft()
        exe = True
    
        for i in prior :
            if now[1] < i[1] :
                exe = False
                break
        if not exe :
            prior.append(now)
        else :
            answer += 1
            if now[0] == location :
                return answer
    
    
    return answer