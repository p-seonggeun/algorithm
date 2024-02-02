def solution(s):
    l = s.split(" ")
    num = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    for i in range(len(l)) :
        if l[i] != "" :
            if l[i][0] not in num :
                l[i] = l[i].capitalize()
    return ' '.join(l)