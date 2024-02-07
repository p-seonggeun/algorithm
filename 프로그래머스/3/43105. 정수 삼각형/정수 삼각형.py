def solution(triangle) :
    answer = 0
    top = 0
    top_left = 0
    for i in range(1, len(triangle)) :
        for j in range(len(triangle[i])) :
            if j != len(triangle[i]) - 1 :
                if i - 1 < 0 :
                    top = 0
                else :
                    top = triangle[i - 1][j]
                if i - 1 < 0 or j - 1 < 0 :
                    top_left = 0
                else :
                    top_left = triangle[i - 1][j - 1]
            else :
                top_left = triangle[i - 1][j - 1]
                
            triangle[i][j] = max(top, top_left) + triangle[i][j]
            
    answer = max(triangle[-1])
    return answer