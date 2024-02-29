def solution(picture, k):
    answer = []
    for i in picture :
        temp = list(i)
        t = ''
        for j in temp :
            t += j * k
        for _ in range(k) :
            answer.append(t)
        
    return answer