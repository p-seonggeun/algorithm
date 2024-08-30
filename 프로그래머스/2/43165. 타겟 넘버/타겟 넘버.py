sign = ["+", "-"]
l = []

def check(t) :
    global target_num
    if sum(t) == target_num :
        return True
    else : return False

def dfs(count) :
    global limit
    global answer
    global list_numbers
    if count == limit :
        if check(l) :
            answer += 1
        return
    
    for i in range(len(sign)) :
        l.append(int(sign[i] + str(list_numbers[count])))
        dfs(count + 1)
        l.pop()
    
def solution(numbers, target):
    global limit
    global answer
    global list_numbers
    list_numbers = numbers
    global target_num
    target_num = target
    
    limit = len(numbers)
    answer = 0
    
    dfs(0)
    
    
    return answer