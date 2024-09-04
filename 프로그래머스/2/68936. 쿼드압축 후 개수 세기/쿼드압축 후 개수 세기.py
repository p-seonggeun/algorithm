def dfs(r, c, n, arr) :
    global one, zero
    if n == 1 :
        if arr[r][c] == 1 :
            one += 1
        else :
            zero += 1
        return
    
    m = n // 2
    
    standard = arr[r][c]
    flag = True
    for i in range(r, r + n) :
        for j in range(c, c + n) :
            if standard != arr[i][j] :
                flag = False
    
    if flag :
        if standard == 1 : one += 1
        else : zero += 1
        return
    
    else :
        dfs(r, c, m, arr)
        dfs(r, c + m, m, arr)
        dfs(r + m, c, m, arr)
        dfs(r + m, c + m, m, arr)
    

def solution(arr):
    global one, zero
    one, zero = 0, 0
    n = len(arr)
    
    dfs(0, 0, n, arr)
    answer = [zero, one]
    return answer