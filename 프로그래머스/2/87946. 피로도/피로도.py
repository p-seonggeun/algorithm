from itertools import permutations
def solution(k, dungeons):
    answer = 0
    for i in list(permutations(dungeons)) :
        t = k
        temp = 0
        
        for j in i :
            if j[0] <= t :
                t -= j[1]
                temp += 1
            else :
                break
        answer = max(answer, temp)
    return answer