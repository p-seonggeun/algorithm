def solution(numbers):
    answer = []
    stack = []
    
    while numbers :
        t = numbers.pop()
        if not stack :
            answer.append(-1)
            stack.append(t)
        else :
            while stack and stack[-1] <= t :
                stack.pop()
            
            if not stack :
                answer.append(-1)
                stack.append(t)
            else :
                answer.append(stack[-1])
                stack.append(t)
            
    
    return answer[::-1]