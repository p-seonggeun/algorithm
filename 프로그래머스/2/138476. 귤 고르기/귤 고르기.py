def solution(k, tangerine):
    answer = 0
    dict = {}
    s = set(tangerine)
    for i in list(s) :
        dict[i] = 0
    
    for i in tangerine :
        dict[i] += 1
    
    values = list(dict.values())
    values.sort(reverse = True)
    
    for i in values :
        k -= i
        answer += 1
        if k <= 0 :
            break
    
    return answer