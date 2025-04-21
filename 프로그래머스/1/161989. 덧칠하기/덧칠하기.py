def solution(n, m, section):
    answer = 0
    for index, i in enumerate(section) :
        
        if index == 0 :
            temp = i
            answer += 1
        else :
            if temp + m - 1 < i :
                answer += 1
                temp = i
    return answer