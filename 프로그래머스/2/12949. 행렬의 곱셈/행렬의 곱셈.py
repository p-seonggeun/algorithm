def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)) :
        t = []
        for j in range(len(arr2[0])) : # arr2 열만큼
            s = 0
            for k in range(len(arr2)) : # arr2 행
                s += arr1[i][k] * arr2[k][j]
            t.append(s)
        answer.append(t)
    
    return answer