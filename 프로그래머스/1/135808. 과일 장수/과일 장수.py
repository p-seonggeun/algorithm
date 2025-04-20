def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    
    l = []
    for i in score :
        l.append(i)
        if len(l) == m :
            answer += l[m - 1] * m
            l = []
    return answer