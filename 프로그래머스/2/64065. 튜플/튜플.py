def solution(s):
    answer = []
    s = s[1:]
    s = s[:len(s) - 1]
    
    l = []
    st = ''
    for index, i in enumerate(s) :
        if i == '{' :
            t = []
            st = ''
        elif i.isnumeric() :
            st += i
        elif i == ',' :
            t.append(st)
            st = ''
        elif i == '}' :
            if index == len(s) - 1 :
                t.append(st)
            l.append(t)
    
    l.sort(key = lambda x : len(x))
    
    s = []
    
    for i in l :
        for j in i :
            if int(j) not in s :
                s.append(int(j))
    return s