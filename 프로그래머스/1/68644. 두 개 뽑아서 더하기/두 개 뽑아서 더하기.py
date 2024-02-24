from itertools import combinations
def solution(numbers):
    answer = []
    numbers.sort()
    l = list(combinations(numbers, 2))
    s = set()
    for i in l :
        s.add(sum(i))
    answer = list(s)
    answer.sort()
    return answer