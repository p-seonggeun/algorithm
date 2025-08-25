def solution(s):
    answer = []
    s = s[1:len(s) - 1]

    l = []
    t = []
    
    for index, i in enumerate(s):
        if i == '{':
            temp = ''
            t = []
        elif i == ',' and s[index + 1].isnumeric():
            t.append(int(temp))
            temp = ''
        elif i == '}':
            t.append(int(temp))
            l.append(t)
        elif i.isnumeric():
            temp += i
    
    l.sort(key = lambda x : len(x))
    for i in l:
        for j in i:
            if j not in answer:
                answer.append(j)
    return answer
