from collections import deque
def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0 :
        return len(cities) * 5
    queue = deque([], cacheSize)
    for i in cities : 
        i = i.lower()
        if i not in queue :
            answer += 5
            queue.appendleft(i)
        else :
            answer += 1
            queue.remove(i)
            queue.appendleft(i)
    return answer