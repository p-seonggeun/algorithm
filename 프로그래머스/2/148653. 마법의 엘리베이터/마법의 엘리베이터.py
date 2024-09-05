def solution(storey):
    answer = 0
    
    while storey != 0 :
        n = storey % 10
        if n > 5 :
            answer += (10 - n)
            storey += 10
        elif n < 5 :
            answer += n
        else :
            if len(str(storey)) >= 2 :
                if int(str(storey)[-2]) >= 5 :
                    answer += (10 - n)
                    storey += 10
                else :
                    answer += n
            else :
                answer += n
        
        storey //= 10
    return answer