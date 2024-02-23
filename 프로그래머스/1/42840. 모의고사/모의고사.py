def solution(answers):
    answer = []

    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    l = [0, 0, 0]
    
    for i in range(len(answers)) :
        if answers[i % len(answers)] == one[i % len(one)] :
            l[0] += 1
    for i in range(len(answers)) :
        if answers[i % len(answers)] == two[i % len(two)] :
            l[1] += 1
    for i in range(len(answers)) :
        if answers[i % len(answers)] == three[i % len(three)] :
            l[2] += 1

    print(l)
    
    m = max(l)
    for index, i in enumerate(l) :
        if i == m :
            answer.append(index + 1)
    
    return answer