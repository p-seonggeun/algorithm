def solution(prices):
    answer = []
    stack = []
    temp = []
    
    for index, i in enumerate(prices) :
        
        while stack and stack[-1][-1] > i :
            t = stack.pop()
            temp.append((t[0], index - t[0]))
        stack.append((index, i))
    
    else :
        while stack :
            t = stack.pop()
            temp.append((t[0], index - t[0]))
        
    temp.sort(key = lambda x : x[0])
    for i in temp :
        answer.append(i[1])
        
    return answer