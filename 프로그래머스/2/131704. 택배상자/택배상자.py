def solution(order):
    answer = 0
    f = []
    m = []
    c = 0
    for i in range(1, len(order) + 1) :
        if i != order[c] :
            m.append(i)
        else :
            f.append(i)
            c += 1
            while m and m[-1] == order[c] :
                f.append(m.pop())
                c += 1
                
    while m and m[-1] == order[c] :
        f.append(m.pop())
        c += 1

    answer = len(f)
    return answer