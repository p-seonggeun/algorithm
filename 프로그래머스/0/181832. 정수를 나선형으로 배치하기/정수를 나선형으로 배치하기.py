def solution(n) :
    answer = []
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    l = [[0] * n for _ in range(n)]
    num = 1
    i, j = 0, 0
    index = 0
    l[i][j] = num
    
    while num < n ** 2 :
        if 0 <= i + direction[index][0] < n and 0 <= j + direction[index][1] < n and \
        l[i + direction[index][0]][j + direction[index][1]] == 0 :
            i += direction[index][0]
            j += direction[index][1]
            num += 1
            l[i][j] = num
        else :
            index += 1
            index = index % 4
    
    return l