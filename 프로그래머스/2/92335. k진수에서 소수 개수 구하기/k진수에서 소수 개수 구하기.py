from math import sqrt
def solution(n, k):
    answer = 0
    
    def prime(n) :
        if n == 1 or n == 0 :
            return False
        for i in range(2, int(sqrt(n)) + 1) :
            if n % i == 0 :
                return False
        return True
    
    temp = []
    while (n > 0) :
        temp.append(str(n % k))
        n = n // k
    temp = temp[::-1]
    temp = ''.join(temp)
    
    temp = temp.split("0")
    print(temp)
    for i in temp :
        if i == '' :
            continue
        if prime(int(i)) :
            answer += 1
    
    return answer