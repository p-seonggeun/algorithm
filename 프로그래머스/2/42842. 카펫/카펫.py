def solution(brown, yellow):
    answer = []
    
    t = []
    for i in range(1, yellow + 1) :
        if i > yellow // i :
            break
        if yellow % i == 0 :
            t.append([yellow // i, i])
    
    for i in t :
        m, n = i
        if (2 * m + 4) + (2 * n) == brown :
            answer = [m + 2, n + 2]
    return answer