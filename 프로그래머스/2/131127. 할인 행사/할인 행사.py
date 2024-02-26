import copy
def solution(want, number, discount):
    answer = 0
    d = {}
    for i, j in zip(want, number) :
        d[i] = j
    
    for i in range(len(discount) - 9) :
        dict = copy.deepcopy(d)   
        for j in range(10) :
            if discount[i + j] not in dict :
                continue
            dict[discount[i + j]] -= 1
        temp = dict.values()
        flag = True
        for i in temp :
            if i > 0 :
                flag = False
                break
        if flag :
            answer += 1
        
    return answer