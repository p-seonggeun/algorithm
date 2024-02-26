def solution(elements):
    answer = set()
    length = len(elements)
    answer.add(sum(elements))
    elements = elements + elements
    
    for i in range(1, length) :
        for j in range(len(elements)) :
            if j - length == i :
                break
            answer.add(sum(elements[j : j + i]))
    answer = len(answer)
    return answer