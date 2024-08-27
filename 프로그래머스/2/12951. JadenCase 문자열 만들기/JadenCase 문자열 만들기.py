def solution(s):
    t = s.split(" ")
    
    for i in range(len(t)) :
        t[i] = t[i].capitalize()

    return " ".join(t)