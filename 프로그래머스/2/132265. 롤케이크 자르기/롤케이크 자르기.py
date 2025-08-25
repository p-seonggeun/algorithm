def solution(topping):
    answer = 0
    
    a = {}
    b = {}
    for i in topping:
        if i in b:
            b[i] += 1
        else:
            b[i] = 1
    
    for i in topping:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
        if i in b:
            b[i] -= 1
            if b[i] == 0:
                del b[i]
        
        if len(a) == len(b):
            answer += 1
    return answer