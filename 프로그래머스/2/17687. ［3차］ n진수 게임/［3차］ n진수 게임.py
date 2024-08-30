d = {10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}
def change(number, n) :
    if number == 0 :
        return "0"
    temp = []
    
    while number > 1 :
        if 10 <= number % n <= 15 :
            temp.append(d[number % n])
        else :
            temp.append(str(number % n))
        number //= n
    
    if number != 0 :
        temp.append(str(number))
    return ''.join(temp[::-1])

def solution(n, t, m, p):
    answer = ''
    
    temp = ''
    for i in range(t * m) :
        temp += change(i, n)
    
    for i in range(p - 1, len(temp), m) :
        answer += temp[i]
        if len(answer) == t :
            break
    
    return answer