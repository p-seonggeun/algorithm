def solution(gems):
    answer = []
    global result
    result = [1, len(gems)]
    
    def check(s, e) :
        if result[1] - result[0] == e - s : # 길이가 같으면 스타트가 작은거
            if s < result[0] :
                result[0] = s + 1
                result[1] = e + 1
        else : # 길이가 다르면 길이가 더 작은거 
            if result[1] - result[0] >= e - s :
                result[0] = s + 1
                result[1] = e + 1
        return result
    
    d = {}
    s, e = 0, 0
    stand = len(set(gems))
    while s <= e and e < len(gems) :
        d[gems[e]] = e
        if len(d) == stand :
            answer = check(s, e)
            if s == d[gems[s]] :
                del d[gems[s]]
            s += 1
        else :
            e += 1
        
    return answer