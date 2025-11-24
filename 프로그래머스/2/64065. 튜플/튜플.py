def solution(s):
    answer = []
    s = s[2:-2]
    temp = s.split("},{")
    temp.sort(key = lambda x : len(x))
    
    for i in temp:
        for j in i.split(","):
            j = int(j)
            if j not in answer:
                answer.append(j)
    return answer