from math import gcd
def solution(arrayA, arrayB):
    answer = 0
    arrayA = list(set(arrayA))
    arrayB = list(set(arrayB))
    
    if len(arrayA) > 1 and len(arrayB) > 1 :
        a, b = gcd(arrayA[0], arrayA[1]), gcd(arrayB[0], arrayB[1])
    else :
        if len(arrayA) == 1 : a = arrayA[0]
        if len(arrayB) == 1 : b = arrayB[0]
    for i in range(len(arrayA) - 1) :
        a = gcd(a, arrayA[i + 1])
    
    for i in range(len(arrayB) - 1) :
        b = gcd(b, arrayB[i + 1])
    
    fa, fb = True, True
    for i in arrayB :
        if i % a == 0 :
            fa = False

    for i in arrayA :
        if i % b == 0 :
            fb = False
    
    if fa and fb :
        answer = max(a, b)
    elif fa and not fb :
        answer = a
    elif fb and not fa :
        answer = b
    else :
        answer = 0
        
    return answer