def solution(citations):
    answer = 0
    
    while True:
        a = []
        b = []
        for i in citations:
            if i >= answer:
                a.append(i)
            else:
                b.append(i)
        
        if len(a) < answer:
            return answer - 1
        answer += 1