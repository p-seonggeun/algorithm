def solution(k, tangerine):
    answer = 0

    d = dict()
    
    for i in tangerine :
        if i in d:
            d[i] += 1
        else : d[i] = 1
    
    l = list(d.items())
    l.sort(key = lambda x : x[1], reverse = True)
    
    for i in l :
        if k <= 0 :
            break
        k -= d[i[0]]
        answer += 1
    return answer