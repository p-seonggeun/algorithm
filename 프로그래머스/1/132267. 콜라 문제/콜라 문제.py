def solution(a, b, n):
    answer = 0
    service = 0
    
    while n >= a :
        service = (n // a) * b
        answer += service
        left = n % a
        n = service + left
    
    return answer