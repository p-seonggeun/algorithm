def solution(progresses, speeds):
    answer = []
    temp = []
    for i, j in zip(progresses, speeds) :
        cnt = 0
        while i < 100 :
            i += j
            cnt += 1
        temp.append(cnt)
        
    l = []
    
    for i in range(len(temp)) :
        num = 1
        if i in l :
            continue
        for j in range(i + 1, len(temp)) :
            if temp[i] >= temp[j] :
                num += 1
                l.append(j)
            else :
                break
        answer.append(num)
    return answer