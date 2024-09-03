def solution(n):
    answer = 0
    d = [0] * (n + 1)
    d[1] = 1
    d[2] = 2
    
    for i in range(3, n + 1) :
        d[i] = (d[i - 2] + d[i - 1]) % 1000000007
    
    answer = d[n]
    return answer