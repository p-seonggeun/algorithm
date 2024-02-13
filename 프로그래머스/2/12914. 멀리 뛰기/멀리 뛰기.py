def solution(n):
    answer = 0
    d = [0] * 2001
    d[1] = 1
    d[2] = 2
    
    for i in range(3, 2001) :
        d[i] = (d[i - 1] + d[i - 2]) % 1234567

    answer = d[n]
    
    return answer