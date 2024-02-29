import math
def solution(a, b):
    answer = 0
    g = math.gcd(a, b)
    a = a // g
    b = b // g
    s = [2, 5]
    while b != 1 :
        for i in range(2, b + 1) :
            if b % i == 0 :
                if i not in s :
                    return 2
                else :
                    b = b // i
                    break

    return 1
    
    return answer