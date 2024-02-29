def solution(arr, queries):
    answer = []
    for s, e, k in queries :
        temp = arr[s:e + 1]
        flag = False
        temp.sort()
        for i in temp :
            if i > k :
                answer.append(i)
                flag = True
                break
        if not flag :
            answer.append(-1)
    return answer