def solution(elements):
    answer = 0
    s = set()
    elements = elements * 2
    for i in range(1, len(elements) // 2 + 1) :
        for j in range(1, len(elements) // 2 + 1) :
            s.add(sum(elements[i:i + j]))
        
    return len(s)