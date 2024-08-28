from collections import deque
def solution(cacheSize, cities):
    answer = 0
    queue = deque(maxlen = cacheSize)
    
    for i in cities :
        i = i.lower()
        if i not in queue :
            answer += 5
            queue.append(i)
        else :
            queue.remove(i)
            answer += 1
            queue.append(i)
    return answer