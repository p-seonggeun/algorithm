def solution(s):
    t = list(map(int, s.split(" ")))
    answer = str(min(t)) + " " + str(max(t))
    return answer