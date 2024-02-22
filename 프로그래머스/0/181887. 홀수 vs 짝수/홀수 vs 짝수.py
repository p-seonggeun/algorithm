def solution(num_list):
    answer = 0
    e, o = 0, 0
    for i in range(len(num_list)) :
        if i % 2 == 0 :
            e += num_list[i]
        else :
            o += num_list[i]
    if e >= o :
        answer = e
    else :
        answer = o
    return answer