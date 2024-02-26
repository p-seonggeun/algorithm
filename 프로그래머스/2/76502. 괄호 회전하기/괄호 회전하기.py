from collections import deque
def solution(s):
    answer = 0
    s = list(s)
    s = deque(s)
    for i in range(len(s)) :
        s.rotate(-1)
        temp = []
        for i in list(s) :
            if len(temp) != 0 :
                if i == ')' and temp[-1] == '(' :
                    temp.pop()
                elif i == ']' and temp[-1] == '[' :
                    temp.pop()
                elif i == '}' and temp[-1] == '{' :
                    temp.pop()
                else :
                    temp.append(i)
            else :
                temp.append(i)
        if len(temp) == 0 :
            answer += 1
    return answer