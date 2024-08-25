def solution(x, y, n):
    answer = 0
    INF = 1e9
    d = [INF] * (y + 1)
    j = 0
    for i in range(x, y + 1, n) :
        d[i] = j
        j += 1

    for i in range(x, y + 1) :
        if i - n >= 0 :
            d[i] = min(d[i], d[i - n] + 1)
        if i % 2 == 0 :
            d[i] = min(d[i], d[i // 2] + 1)
        if i % 3 == 0 :
            d[i] = min(d[i], d[i // 3] + 1)
        if i % 6 == 0 :
            d[i] = min(d[i], d[i // 2] + 1, d[i // 3] + 1)
    
    if d[y] == INF :
        return -1
    else :
        return d[y]