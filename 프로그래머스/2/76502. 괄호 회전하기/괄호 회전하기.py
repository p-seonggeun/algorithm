def check(l) :
    t = []
    l = list(l)
    for i in l :
        if not t:
            t.append(i)
        else :
            if (i == ')' and t[-1] =='(') or (i == ']' and t[-1] == '[') or (i == '}' and t[-1] == '{') :
                t.pop()
            else :
                t.append(i)
    if t : return False
    else : return True
            
from collections import deque            
def solution(s):
    answer = 0
    queue = deque(s)
    for i in range(len(s)) :
        queue.rotate(-i)
        if check(queue) :
            answer += 1
        queue.rotate(i)
    return answer