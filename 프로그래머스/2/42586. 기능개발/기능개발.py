def solution(progresses, speeds):
    answer = []
    t = []
    
    for i, j in zip(progresses, speeds) :
        c = 0
        while i < 100 :
            i += j
            c += 1
        t.append(c)
    
    temp = []
    for i in range(len(t)) :
        if i in temp : continue
        c = 0
        for j in range(i, len(t)) :
            if t[j] > t[i] :
                answer.append(c)
                break
            else :
                c += 1
                temp.append(j)
        else :
            answer.append(c)
            
            
    return answer