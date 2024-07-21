def solution(numbers, target):
    def dfs(index, count) :
        global answer
        if count == len(numbers) :
            if sum(l) == target:
                answer += 1
            return

        for i in range(len(sign)) :
            l.append(int(sign[i] + numbers[count]))
            dfs(i, count + 1)
            l.pop()
            
    global answer        
    answer = 0            
    sign = ["+", "-"]
    numbers = list(map(str, numbers))
    l = []
    dfs(0, 0)
    
    
    return answer