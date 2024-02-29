def solution(l, r):
    answer = []
    p = [1, 2, 3, 4, 6, 7, 8, 9]
    for i in range(l, r + 1) :
        s = set(list(str(i)))
        flag = True
        for j in s :
            if int(j) in p :
                flag = False
                break
        if flag :
            answer.append(i)
    if not answer :
        answer.append(-1)
    return answer