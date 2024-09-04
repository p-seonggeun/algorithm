s = { 0 : 'd', 1 : 'r', 2 : 'u' }
d = { 'u' : [-1, -1], 'd' : [1, 0], 'r' : [0, 1] }
def solution(n):
    answer = []
    l = []
    for i in range(1, n + 1) :
        t = [0 for _ in range(i)]
        l.append(t)
    
    k = 1
    r, c = 0, 0
    l[r][c] = k
    p = 0
    
    direction = d[s[p % 3]]     
    for i in range(n - 1) :
        k += 1
        r += direction[0]
        c += direction[1]
        l[r][c] = k
    p += 1
    
    for i in range(n - 1, -1, -1) :
        direction = d[s[p % 3]]     
        for j in range(i) :
            k += 1
            r += direction[0]
            c += direction[1]
            l[r][c] = k
        p += 1
    
    for i in l:
        for j in i :
            answer.append(j)
        
    return answer