def solution(n):
    answer = 0
    l = [i + 1 for i in range(n)]
    
    for i in range(n) :
        temp = 0
        for j in range(i, n) :
            if temp == n :
                answer += 1
                break
            elif temp > n :
                break
            temp += l[j]
    return answer + 1