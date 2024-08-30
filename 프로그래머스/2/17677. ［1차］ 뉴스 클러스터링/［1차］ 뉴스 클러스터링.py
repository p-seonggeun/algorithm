def solution(str1, str2):
    answer = 0
    l1, l2 = [], []
    
    for i in range(len(str1) - 1) :
        t = str1[i : i + 2]
        if t.isalpha() :
            l1.append(t.lower())
    
    for i in range(len(str2) - 1) :
        t = str2[i : i + 2]
        if t.isalpha() :
            l2.append(t.lower())
    
    d1, d2 = {}, {}
    for i in l1 :
        if i in d1 :
            d1[i] += 1
        else : d1[i] = 1
    
    for i in l2 :
        if i in d2 :
            d2[i] += 1
        else : d2[i] = 1
    
    print(d1, d2)
    s = set()
    for i in l1 :
        if i not in s :
            s.add(i)
    
    for i in l2 :
        if i not in s :
            s.add(i)
    
    union, intersection = [], []
    for i in s :
        if i in d1 and i in d2 :
            for _ in range(min(d1[i], d2[i])) :
                intersection.append(i)
            for _ in range(max(d1[i], d2[i])) :
                union.append(i)
        else :
            if i in d1 :
                for _ in range(d1[i]) :
                    union.append(i)
            else :
                for _ in range(d2[i]) :
                    union.append(i)
    
    if intersection and union :
        answer = int((len(intersection) / len(union)) * 65536)
    elif intersection or (intersection == union):
        return 65536
    else :
        return 0
    return answer