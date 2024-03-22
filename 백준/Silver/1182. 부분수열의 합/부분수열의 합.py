def dfs(n, temp_sum, cnt) :
    global answer
    if n == N :
        if temp_sum == S and cnt > 0 :
            answer += 1
        return
    
    dfs(n + 1, temp_sum + l[n], cnt + 1)
    dfs(n + 1, temp_sum, cnt)

N, S = map(int, input().split())
l = list(map(int, input().split()))
answer = 0
dfs(0, 0, 0)
print(answer)