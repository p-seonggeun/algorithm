dictionary = {10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}
def change(num, n) :
    s = ''
    if num == 0 :
        return '0'
    while num >= 1 :
        if 10 <= num % n <= 15 :
            s += dictionary[num% n]
        else :
            s += str(num % n)
        num = num // n
    return s[::-1]

def solution(n, t, m, p):
    answer = ''
    temp = ''
    for i in range(0, t * m + 1) :
        temp += change(i, n)
    
    for i in range(p - 1, len(temp), m) :
        if len(answer) == t :
            break
        answer += temp[i]
        
    
    return answer