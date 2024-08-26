def solution(s):
    l = []
    
    for i in s :
        if l :
            if l[-1] == '(' and i == ')' :
                l.pop()
            else : l.append(i)
        else :
            l.append(i)
    
    if l : return False
    else : return True