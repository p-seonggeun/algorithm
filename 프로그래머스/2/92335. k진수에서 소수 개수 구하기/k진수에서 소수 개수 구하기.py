

def isPrime(number) :
    if number <= 1 :
        return False
    count = 0
    number = int(number)
    for i in range(2, int(number ** 0.5) + 1) :
        if number % i == 0 :
            return False
    return True

def change(number, k) :
    l = []
    while number >= 1 :
        l.append(str(number % k))
        number //= k
    
    return ''.join(l[::-1])

def solution(n, k):
    answer = 0
    
    t = change(n, k)
    l = []
    s = ''
    for i in range(len(t)) :
        if t[i] != '0' :
            s += t[i]
        else :
            if s :
                l.append(s)
                s = ''
                l.append('0')
            else : l.append('0')
    else :
        if s : l.append(s)
    
    l = list(map(int, l))
    
    for index, i in enumerate(l) :
        if isPrime(i) :
            if len(l) == 1 :
                answer += 1
            else :
                if index == 0 :
                    if l[index + 1] == 0 : answer += 1
                elif index == len(l) - 1 :
                    if l[index - 1] == 0 : answer += 1
                elif len(l) >= 3 :
                    if l[index - 1] == l[index + 1] == 0 : answer += 1
    
    return answer