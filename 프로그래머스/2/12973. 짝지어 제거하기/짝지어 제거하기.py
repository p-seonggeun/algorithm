def solution(s):
    answer = -1

    l = []
    for i in s :
        if l :  
            if l[-1] == i :
                l.pop()
            else :
                l.append(i)
        else :
            l.append(i)
    
    if l : return 0
    else : return 1
    