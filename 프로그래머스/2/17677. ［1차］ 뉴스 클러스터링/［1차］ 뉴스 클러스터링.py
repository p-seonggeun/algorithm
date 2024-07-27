from collections import Counter
def solution(str1, str2):
    answer = 0
    a, b = [], []
    for i in range(len(str1) - 1) :
        temp = str1[i : i + 2]
        if (temp.isalpha()):
            a.append(temp.upper())
        
    for i in range(len(str2) - 1) :
        temp = str2[i : i + 2]
        if temp.isalpha() :
            b.append(temp.upper())
    
    a = Counter(a)
    b = Counter(b)
    
    if sum((a | b).values()) == 0 :
        return 65536
    answer = int((sum((a & b).values()) / sum((a | b).values())) * 65536)
    return answer
    