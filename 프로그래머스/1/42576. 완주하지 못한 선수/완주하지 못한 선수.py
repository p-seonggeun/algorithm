def solution(participant, completion):
    answer = ''
    dic = {}
    for i in participant :
        if i in dic :
            dic[i] += 1
        else :
            dic[i] = 1
            
    for i in completion :
        if i in dic :
            dic[i] -= 1
    
    for x, y in dic.items() :
        if y != 0 :
            answer += x
    return answer