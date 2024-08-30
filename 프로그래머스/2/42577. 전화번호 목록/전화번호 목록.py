def solution(phone_book):
    answer = True
    
    s = set(phone_book)
    
    for i in phone_book :
        t = ""
        for j in i :
            t += j
            if t != i and t in s :
                return False
    
    return answer