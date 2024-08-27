def solution(n):
    answer = 0
    
    for i in range(1, n + 1) :
        t = 0
        for j in range(i, n + 1) :
            t += j
            if t > n :
                break
            elif t == n :
                t = 0
                answer += 1
                break
    return answer