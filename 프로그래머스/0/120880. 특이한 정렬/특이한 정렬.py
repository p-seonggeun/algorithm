def solution(numlist, n):
    answer = []
    temp = []
    for i in numlist :
        temp.append((abs(n - i), i))
    temp.sort(key = lambda x : (x[0], -x[1]))
    for i in temp :
        answer.append(i[1])
    return answer