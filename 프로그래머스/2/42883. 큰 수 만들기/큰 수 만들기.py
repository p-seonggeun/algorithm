def solution(number, k):
    answer = ''
    stack = []
    t = len(number) - k
    for i in number :
        while stack and stack[-1] < i and k > 0 :
            stack.pop()
            k -= 1
        stack.append(i)
    
    answer = ''.join(stack)[:t]
    return answer