def solution(n, k):
    answer = []
    l = [i + 1 for i in range(n)]
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, n + 1) :
        dp[i] = dp[i - 1] * i
    
    print(dp)
    print(l)
    
    while n != 0 :
        answer.append(l[(k - 1) // dp[n - 1]])
        l.remove(l[(k - 1) // dp[n - 1]])
        k = k % dp[n - 1]
        n -= 1
    
    return answer