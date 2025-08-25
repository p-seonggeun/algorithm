def solution(numbers):
    answer = [-1] * len(numbers)
    
    l = []
    for i in range(len(numbers) - 1, -1, -1):
        n = numbers[i]
        
        while l and l[-1] <= n:
            l.pop()
        if l:
            answer[i] = l[-1]
        
        l.append(n)
    return answer