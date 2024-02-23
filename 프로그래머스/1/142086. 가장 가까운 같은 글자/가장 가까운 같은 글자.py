def solution(s):
    answer = []
    temp = []
    l = []
    for i in s :
        temp.append(i)
        if i not in l :
            l.append(i)
            answer.append(-1)
        else :
            count = 0
            for j in range(len(temp) - 2, -1, -1) :
                count += 1
                if i == temp[j] :
                    answer.append(count)
                    break
    return answer