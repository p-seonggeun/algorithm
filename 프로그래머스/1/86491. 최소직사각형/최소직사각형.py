def solution(sizes):
    answer = 0
    for i in sizes :
        if i[0] < i[1] :
            i[0], i[1] = i[1], i[0]
    max1, max2 = 0, 0
    for i, j in sizes :
        max1 = max(max1, i)
        max2 = max(max2, j)
    answer = max1 * max2
    return answer