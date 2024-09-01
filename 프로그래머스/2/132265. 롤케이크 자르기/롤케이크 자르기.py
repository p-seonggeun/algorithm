def solution(topping):
    answer = 0
    d = {}
    
    for i in topping :
        if i in d : d[i] += 1
        else : d[i] = 1
    
    b = {}
    for index, i in enumerate(topping) :
        if i in b : 
            b[i] += 1
        else : b[i] = 1
        
        if i in d :
            if d[i] >= 1 :
                d[i] -= 1
        
        if d[i] == 0 :
            del d[i]
        
        if len(d) == len(b) : answer += 1
        
        
    return answer