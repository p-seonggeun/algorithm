def solution(a, b):
    answer = ''
    l = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    s = 5
    for i in range(a - 1) :
        s += days[i]
    s += b - 1
    return l[s % 7] 