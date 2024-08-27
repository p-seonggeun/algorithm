def solution(n):
    ans = 0
    if n % 2 != 0 :
        n -= 1
        ans += 1

    while n != 0 :
        n //= 2
        if n % 2 != 0 :
            n -= 1
            ans += 1
    
    print(n, ans)
    return ans