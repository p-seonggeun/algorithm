from itertools import permutations
def solution(k, dungeons) :
    answer = 0
    for i in list(permutations(dungeons)) :
        s = k
        t = 0
        for j in i :
            if j[0] <= s:
                t += 1
                s -= j[1]
        answer = max(answer, t)
        
    return answer