def solution(s):
    answer = []
    remove_count = 0
    change_count = 0
    
    
    while s != '1' :
        new_s = ""
        for i in s :
            if i == '0' :
                remove_count += 1
            else :
                new_s += i
    
        c = len(new_s)
        s = bin(c)[2:]
        
        change_count += 1
    answer.append(change_count)
    answer.append(remove_count)
    return answer