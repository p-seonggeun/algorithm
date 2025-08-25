from itertools import product
def solution(word):
    answer = 0
    aeiou = ['A','E','I','O','U']
    
    l = []
    for i in range(1, 6):
        for j in product(aeiou, repeat = i):
            l.append(''.join(list(j)))
    l.sort()
    
    answer = l.index(word) + 1
    return answer