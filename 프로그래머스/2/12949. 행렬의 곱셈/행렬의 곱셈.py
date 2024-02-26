def solution(arr1, arr2):
    answer = []
    n, m = len(arr1), len(arr1[0])
    
    for i in range(n) :
        temp = []
        for j in range(len(arr2[0])) :
            s = 0
            for k in range(len(arr2)) :
                s += (arr1[i][k] * arr2[k][j])
            temp.append(s)
        answer.append(temp)
    
    return answer