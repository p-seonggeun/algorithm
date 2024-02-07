def solution(spell, dic):
    answer = 0
    
    for i in dic :
        dict = {}
        for k in spell :
            dict[k] = 0
        
        for j in spell :
            dict[j] = i.count(j)
        
        if 0 not in list(dict.values()) :
            return 1
    
    return 2