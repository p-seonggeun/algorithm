def solution(land):
    answer = 0
    N = len(land)
    for i in range(1, N) :
        for j in range(4) :
            if j == 0 :
                land[i][j] += max(land[i - 1][j + 1], land[i - 1][j + 2], land[i - 1][j + 3])
            elif j == 1 :
                land[i][j] += max(land[i - 1][j - 1], land[i - 1][j + 1], land[i - 1][j + 2])
            elif j == 2 :
                land[i][j] += max(land[i - 1][j - 2], land[i - 1][j - 1], land[i - 1][j + 1])
            elif j == 3 :
                land[i][j] += max(land[i - 1][j - 3], land[i - 1][j - 2], land[i - 1][j - 1])
    
    answer = max(land[-1])
    
    return answer