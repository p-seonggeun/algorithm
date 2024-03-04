def solution(s):
    answer = 0
    min_length = len(s)
    for i in range(1, len(s) // 2 + 1) : # 반복길이
        temp, same_count = '', 0
        for j in range(0, len(s) - i + 1, i) :
            if j == 0 :
                old = s[j : j + i]
            if old == s[j : j + i] :
                same_count += 1
            else :
                if same_count > 1 :
                    temp += str(same_count) + old
                else :
                    temp += old
                old = s[j : j + i]
                same_count = 1
        
        if same_count > 1 :
            temp += str(same_count) + old
        else :
            temp += old
        
        if len(s) % i != 0 :
            temp += s[(len(s) // i) * i :]
            
        if len(temp) <= min_length :
            min_length = len(temp)
    
    answer = min_length
    return answer