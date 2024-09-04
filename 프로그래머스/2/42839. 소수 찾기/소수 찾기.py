def check(number) :
    if number == 0 or number == 1 :
        return False
    for i in range(2, int(number ** 0.5) + 1) :
        if number % i == 0 :
            return False
    return True

def dfs(t, count, k, visited) :
    global s, l
    if k == count :
        temp = int(''.join(t))
        if check(temp) :
            s.add(temp)
        return
    
    for i in range(len(l)) :
        if visited[i] == False :
            t.append(l[i])
            visited[i] = True
            dfs(t, count + 1, k, visited)
            t.pop()
            visited[i] = False

def solution(numbers) :
    global s, l
    s = set()
    answer = 0
    l = list(numbers)
    
    for i in range(1, len(l) + 1) :
        visited = [False] * len(l)
        t = []
        dfs(t, 0, i, visited)
    
    answer = len(s)
    return answer