def solution(elements):
    answer = 0
    s = set()
    for i in range(len(elements)) :
        temp = elements[i]
        s.add(temp)
        for j in range(i + 1 , i + len(elements)) :
            temp += elements[j % len(elements)]
            s.add(temp)
    
    answer = len(s)
    return answer