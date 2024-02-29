def solution(n, info):
    answer = []
    p = []
    result = [0] * 11
    
    def score(p) :
        ap = 0
        ri = 0
        for i in range(11) :
            if info[i] >= 1 and i not in p :
                ap += 10 - i
            elif i in p :
                ri += 10 - i
        if ri > ap :
            return ri - ap
        else :
            return False
    
    def dfs(index, count) :
        if count == n :
            x = score(p)
            if x :
                answer.append([x, p[::-1]].copy())
            return
        elif count > n :
            if p[-1] == 10 :
                x = score(p)
                if x :
                    answer.append([x, p[::-1]].copy())
            return
                    
        for i in range(index, 11) :
            count += (info[i] + 1)
            p.append(i)
            dfs(i, count)
            count -= (info[i] + 1)            
            p.pop()
        return
    
    dfs(0, 0)
    
    answer.sort(key = lambda x : (x[0], x[1]), reverse = True)

    if answer :
        temp = answer[0]
        score_list = temp[1][::-1]
        for i in score_list :
            result[i] = info[i] + 1
        if sum(result) > n :
            result[-1] -= sum(result) - n
        return result
    else :
        return [-1]
    
    
    return answer