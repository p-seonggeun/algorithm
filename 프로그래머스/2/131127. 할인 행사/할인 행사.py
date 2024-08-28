def solution(want, number, discount):
    answer = 0
    d = {}
    for i, j in zip(want, number) :
        d[i] = j
    
    for i in range(len(discount) - 10 + 1) :
        t = {}
        for j in range(i, i + 10) :
            if discount[j] in t :
                t[discount[j]] += 1
            else : t[discount[j]] = 1
        
        if d == t : answer += 1
    
    return answer