def solution(n, a, b):
    answer = 1
    s = n
    f = 0
    if a > b :
        a, b = b, a
        
    while s != 1 :
        s //= 2
        f += 1
    
    mid = n // 2
    left = 1
    right = n
    c = 1
    while True :
        if a <= mid and b > mid :
            break
        
        elif a <= mid and b <= mid :
            right = mid
            mid = (left + right) // 2
        
        elif a > mid and b > mid :
            left = mid + 1
            mid = (left + right) // 2
        
        c += 1
    
    answer = f - c + 1
    return answer