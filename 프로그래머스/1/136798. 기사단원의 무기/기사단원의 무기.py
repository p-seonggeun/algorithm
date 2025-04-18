def solution(number, limit, power):
    answer = 0
    
    def getCount(a) :
        n = 0
        for i in range(1, int(a ** 0.5) + 1) :
            if a % i == 0 :
                if i == a // i :
                    n += 1
                else :
                    n += 2
        return n
    
    for i in range(1, number + 1) :
        num = getCount(i)
        if num > limit :
            answer += power
        else :
            answer += num
            
    return answer