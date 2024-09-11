from itertools import combinations
def solution(orders, course):
    answer = []
    d = {}
    for i in course :
        d[i] = {}
    for i in orders :
        t = list(i)
        t.sort()
        for j in course :
            if len(t) < j : continue
            for k in combinations(t, j) :
                if k in d[j] : d[j][k] += 1
                else : d[j][k] = 1
    
    temp = {}
    for i in course :
        temp[i] = []
        for j in d[i] :
            if d[i][j] >= 2 :
                temp[i].append([j, d[i][j]])
    
    for i in temp :
        temp[i].sort(key = lambda x : (len(x[0]), -x[1]))
    
    for i in course :
        for j in temp :
            if i == j :
                for index, k in enumerate(temp[j]) :
                    if index == 0 :
                        m = k[1]
                    if m == k[1] :
                        answer.append(''.join(k[0]))
                        
    answer.sort()
    return answer