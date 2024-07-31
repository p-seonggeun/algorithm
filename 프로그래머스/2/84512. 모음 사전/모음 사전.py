from itertools import product
def solution(word):
    answer = 0
    alpha = ["A", "E", "I", "O", "U"]
    l = []
    for i in range(1, 6) :
        for j in list(product(alpha, repeat = i)) :
            l.append(j)
    
    l.sort(key = lambda x : (x, len(x)))
    for index, i in enumerate(l) :
        if "".join(i) == word :
            answer = index + 1
            break
    return answer