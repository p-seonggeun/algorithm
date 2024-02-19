def solution(lottos, win_nums):
    answer = []
    s_l = set(lottos)
    s_w = set(win_nums)
    dict = { 6 : 1, 5 : 2, 4 : 3, 3 : 4, 2 : 5, 1 : 6, 0 : 6}
    zero = lottos.count(0)
    correct = 0
    for i in s_l :
        if i in s_w :
            correct += 1
    
    high = correct + zero
    low = correct
    if high > 6 :
        high = 6
    answer = [dict[high], dict[low]]
    return answer