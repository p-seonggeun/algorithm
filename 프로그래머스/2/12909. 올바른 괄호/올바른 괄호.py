def solution(s):
    answer = True
    l = []
    for i in range(len(s)) :
        if i == 0 :
            if s[i] == ')' :
                return False
            else :
                l.append(s[i])
        else :
            if s[i] == ')' :
                if l :
                    if l[-1] == '(' :
                        l.pop()
                else :
                    return False
            else :
                l.append(s[i])
    if l :
        return False
    return True