from itertools import combinations
def bs(array, target) :
    start = 0
    end = len(array) - 1
    while start <= end :
        mid = int((start + end) / 2)
        if array[mid] < target :
            start = mid + 1
        else :
            end = mid - 1
    return len(array) - start
        
def solution(info, query):
    # 언어 and 직군 and 경력 and 소울푸드 점수
    answer = []
    inf = []
    quer = []
    dict = {}
    for i in info :
        inf.append(i.split(" "))
    
    for i in query :
        i = i.replace("and", "")
        i = i.replace("  ", " ")
        quer.append(i.split(" "))
    
    for i in inf :
        k, v = i[:4], int(i[4])
        
        # 0칸짜리 -
        if ''.join(k) in dict :
            dict[''.join(k)].append(v)
        else :
            dict[''.join(k)] = [v]
            
        # 1칸짜리 -
        for j in range(len(k)) :
            temp = k.copy()
            temp[j] = '-'
            temp = ''.join(temp)
            if temp in dict :
                dict[temp].append(v)
            else :
                dict[temp] = [v]
        
        # 2칸짜리 -
        for m in range(len(k) - 1) :
            for n in range(m + 1, len(k)) :
                temp = k.copy()
                temp[m] = '-'
                temp[n] = '-'
                temp = ''.join(temp)
                if temp in dict :
                    dict[temp].append(v)
                else :
                    dict[temp] = [v]
        
        # 3칸짜리 -
        for j in range(len(k) - 2) :
            for m in range(j + 1, len(k) - 1) :
                for n in range(m + 1, len(k)) :
                    temp = k.copy()
                    temp[j] = '-'
                    temp[m] = '-'
                    temp[n] = '-'
                    temp = ''.join(temp)
                    if temp in dict :
                        dict[temp].append(v)
                    else :
                        dict[temp] = [v]
        # 4칸짜리 -
        temp = k.copy()
        temp[0] = '-'
        temp[1] = '-'
        temp[2] = '-'
        temp[3] = '-'
        temp = ''.join(temp)
        if temp in dict :
            dict[temp].append(v)
        else :
            dict[temp] = [v]
    
    for i, j in dict.items() :
        j.sort()
        
    for i in quer :
        k, v = ''.join(i[:4]), int(i[4])
        if k in dict :
            answer.append(bs(dict[k], v))
        else :
            answer.append(0)
    
    return answer