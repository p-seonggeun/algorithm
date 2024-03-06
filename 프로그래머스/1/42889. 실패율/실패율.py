def solution(N, stages):
    answer = []
    clear = [0] * (N + 2)
    temp = []
    for i in stages :
        clear[i] += 1
        
    for i in range(1, N + 1) :
        if sum(clear[i:]) != 0 :
            temp.append([i, clear[i] / sum(clear[i:])])
        else :
            temp.append([i, 0])
    
    temp.sort(key = lambda x : (-(x[1]), x[0]))
    
    for i in temp :
        answer.append(i[0])
    
    return answer