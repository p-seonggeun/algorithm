def solution(n, bans):
    nums = []
    for i in bans:
        t = 0
        for index, j in enumerate(i):
            t += (26 ** (len(i) - 1 - index)) * (ord(j) - 97 + 1)
        nums.append(t)
    nums.sort()
    
    for i in nums:
        if n >= i:
            n += 1
        else:
            break
    
    answer = ""
    while n > 0:
        n -= 1
        answer = chr(97 + (n % 26)) + answer
        n //= 26        
            
    return answer