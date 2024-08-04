def solution(topping):
    answer = 0
    d_c = {}
    for i in topping :
        if i in d_c :
            d_c[i] += 1
        else : d_c[i] = 1
    
    index = len(topping) - 1
    d_d = {}
    while index >= 0 :
        if index == -1 :
            break
        
        if d_c[topping[index]] > 0 :
            d_c[topping[index]] -= 1
            if d_c[topping[index]] == 0 :
                del d_c[topping[index]]
        
        if topping[index] in d_d :
            d_d[topping[index]] += 1
        else : d_d[topping[index]] = 1
        
        if len(d_c) == len(d_d) : answer += 1
        
        index -= 1
        
    return answer