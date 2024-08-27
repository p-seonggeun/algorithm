def solution(s):
    a, b = 0, 0
    while s != '1' :
        t = len(s)
        s = s.replace("0", "")
        b += t - len(s)
        
        s = bin(len(s))[2:]
        
        a += 1
    
    return [a, b]