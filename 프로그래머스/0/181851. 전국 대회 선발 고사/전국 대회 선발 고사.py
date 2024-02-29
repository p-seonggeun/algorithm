def solution(rank, attendance):
    answer = 0
    temp_rank = sorted(rank)
    temp_attend = []
    for i in temp_rank :
        if attendance[rank.index(i)] :
            temp_attend.append(rank.index(i))
    answer = temp_attend[0] * 10000 + temp_attend[1] * 100 + temp_attend[2]
    return answer