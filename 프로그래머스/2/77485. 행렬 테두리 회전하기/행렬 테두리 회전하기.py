def solution(rows, columns, queries):
    answer = []
    l = []
    temp = []
    for i in range(rows * columns) :
        temp.append(i + 1)
        if len(temp) == columns :
            l.append(temp)
            temp = []
    
    for i in queries :
        x1, y1, x2, y2 = i[0] - 1, i[1] - 1, i[2] - 1, i[3] - 1
        t = l[x1][y2]
        m = l[x1][y2]

        # 위
        for j in range(y2, y1, -1) :
            l[x1][j] = l[x1][j - 1]
            m = min(m, l[x1][j])
        # 왼
        for j in range(x1, x2) :
            l[j][y1] = l[j + 1][y1]
            m = min(m, l[j][y1])
        # 아 
        for j in range(y1, y2) :
            l[x2][j] = l[x2][j + 1]
            m = min(m, l[x2][j])
        # 오
        for j in range(x2, x1, -1) :
            l[j][y2] = l[j - 1][y2]
            m = min(m, l[j][y2])
        
        answer.append(m)
        l[x1 + 1][y2] = t
        
    return answer