from itertools import combinations

def solution(clothes):
    answer = 0
    dict = {}
    for i in clothes :
        if i[1] in dict :
            dict[i[1]].append(i[0])
        else :
            dict[i[1]] = [i[0]]
            
    dk = list(dict.keys())
    dv = list(dict.values())
    flag = True
    
    for i in dv :
        if len(i) != 1 :
            flag = False
            break
            
    if flag :
        return 2 ** len(dk) - 1
    
    temp = []
    for i in range(1, len(dk) + 1) :
        for j in (list(combinations(dk, i))) :
            temp.append(j)

    for i in temp :
        t = 1
        for j in i :
            t *= (len(dict[j]))
        answer += t
    
    return answer