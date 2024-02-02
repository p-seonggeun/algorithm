def solution(s):
    s = list(map(int, s.split(' ')))
    mi, ma = min(s), max(s)
    result = str(mi) + " " + str(ma)
    return result