def solution(numbers):
    answer = []
    
    def check(l) :
        m = len(l) // 2
        if len(l) >= 3 :
            if l[m] == '1' :
                if check(l[:m]) and check(l[m + 1:]) :
                    return True
                else :
                    return False
            else :
                if '1' in l :
                    return False
                else :
                    return True
        else :
            return True
    for i in numbers :
        temp = str(bin(i)[2:])
        length = len(temp)
        count = 0
        
        while (length + 1 + count) & (length + count) != 0 :
            count += 1
        
        temp = '0' * count + temp # 이것의 길이가 2 ** n - 1
        
        if check(temp) :
            answer.append(1)
        else :
            answer.append(0)
            
    return answer

