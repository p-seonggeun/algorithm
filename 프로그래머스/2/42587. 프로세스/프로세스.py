from collections import deque
def solution(priorities, location):
    answer = 0
    l = []
    
    stand = []
    for index, i in enumerate(priorities) :
        l.append([i, index])
        if index == location :
            stand = [i, index]
    
    
    priorities.sort(reverse = True)
    
    queue_p = deque(priorities)
    queue = deque(l)
    count = 0
    
    while True :
        t = queue.popleft()
        if t[0] == queue_p[0] :
            queue_p.popleft()
            count += 1
            if t[1] == stand[1] :
                break
        else :
            queue.append(t)
    
    return count