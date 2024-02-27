def solution(cap, n, deliveries, pickups):
    answer = 0
    
    temp = 0
    d = []
    for i in range(n - 1, -1, -1) :
        if temp == 0 and deliveries[i] != 0 :
            temp = cap
            d.append(i + 1)
        while temp != 0 :
            if deliveries[i] == 0 :
                break
            if deliveries[i] > temp :
                deliveries[i] -= temp
                temp = cap
                d.append(i + 1)
            else :
                temp -= deliveries[i]
                deliveries[i] = 0
    
    temp = 0
    p = []
    for i in range(n - 1, -1, -1) :
        if temp == 0 and pickups[i] != 0 :
            temp = cap
            p.append(i + 1)
        while temp != 0 :
            if pickups[i] == 0 :
                break
            if pickups[i] > temp :
                pickups[i] -= temp
                temp = cap
                p.append(i + 1)
            else :
                temp -= pickups[i]
                pickups[i] = 0
    
    if len(d) > len(p) :
        for i, j in zip(d, p) :
            answer += max(i, j) * 2
        for i in range(len(p), len(d)) :
            answer += d[i] * 2
    elif len(d) == len(p) :
        for i, j in zip(d, p) :
            answer += max(i, j) * 2
    else :
        for i, j in zip(d, p) :
            answer += max(i, j) * 2
        for i in range(len(d), len(p)) :
            answer += p[i] * 2

    return answer