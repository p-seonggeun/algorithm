def solution(s):
    answer = []
    s = s[1:]
    s = s[:len(s) - 1]
    l = []
    temp = []
    n = ''
    for i in s :
        if i == '{' :
            continue
        elif i == '}' :
            temp.append(int(n))
            n = ''
            l.append(temp)
            temp = []
        elif i == ',' :
            if n != '' :
                temp.append(int(n))
                n = ''
        else :
            n += i
            
    l.sort(key = lambda x : len(x))
    
    for i in l :
        for j in i :
            if j not in answer :
                answer.append(j)
            
    
    return answer