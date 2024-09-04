def solution(sequence, k):
    answer = []
    s, e = 0, 0
    hap = sequence[e]
    t = []
    while s <= e :
        if hap == k :
            t.append([s, e])
        
        if s == e == len(sequence) - 1 :
            break
        
        if hap < k :
            if e + 1 < len(sequence) :        
                e += 1
                hap += sequence[e]
            else :
                break
        
        elif hap >= k :
            hap -= sequence[s]
            if s + 1 < len(sequence) :
                s += 1
            else :
                break
            
    t.sort(key = lambda x : (x[1] - x[0]))
    answer = t[0]
    
    return answer