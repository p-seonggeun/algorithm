def solution(land):
    answer = 0
    
    d = [[0 for _ in range(4)] for _ in range(len(land))]
    d[0][0] = land[0][0]
    d[0][1] = land[0][1]
    d[0][2] = land[0][2]
    d[0][3] = land[0][3]
    
    for i in range(1, len(land)) :
        d[i][0] = max(d[i - 1][1], d[i - 1][2], d[i - 1][3]) + land[i][0]
        d[i][1] = max(d[i - 1][0], d[i - 1][2], d[i - 1][3]) + land[i][1]
        d[i][2] = max(d[i - 1][0], d[i - 1][1], d[i - 1][3]) + land[i][2]
        d[i][3] = max(d[i - 1][0], d[i - 1][1], d[i - 1][2]) + land[i][3]
    
    answer = max(d[len(land) - 1])
    return answer