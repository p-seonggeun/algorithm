def change(number) :
    t = []
    while number >= 1 :
        number, r = number // 3, number % 3
        if r == 0 :
            number -= 1
            r += 3
        t.append(str(r))
    
    return ''.join(t[::-1])
        

def solution(n):
    answer = ''
    s = change(n)
    answer = s.replace("3", "4")
    
    return answer