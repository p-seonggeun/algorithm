def solution(clothes):
    answer = 1
    d = {}
    
    for i in clothes :
        if i[1] in d :
            d[i[1]].append(i[0])
        else :
            d[i[1]] = [i[0]]
    
    for i in d :
        answer *= len(d[i]) + 1

    return answer - 1