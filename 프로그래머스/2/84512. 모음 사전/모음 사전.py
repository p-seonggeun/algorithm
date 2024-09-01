def solution(word):
    global c
    answer = 0
    d = ['A', 'E', 'I', 'O', 'U']
    p = {}
    c = 1
    t = []
    def dfs(count) :
        global c
        if count == 5 :
            return
    
        for i in range(len(d)) :
            t.append(d[i])
            p[''.join(t[::])] = c
            c += 1
            dfs(count + 1)
            t.pop()
    
    dfs(0)
    answer = p[word]
    return answer