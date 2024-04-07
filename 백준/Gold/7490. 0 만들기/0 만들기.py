def calc(stack, N) :
    stack = [0] + stack
    answer = ''
    for i in range(1, N + 1) :
        answer += str(i)
        if i != N :
            answer += stack[i]
    temp = answer.replace(" ", "")
    if eval(temp) == 0 :
        return answer
    
def dfs(count) :
    if count == N - 1 :
        answer = calc(stack, N)
        if answer != None :
            print(answer)
        return
    
    for i in range(len(l)) :
        stack.append(l[i])
        dfs(count + 1)
        stack.pop()

T = int(input())
l = [' ', '+', '-']
stack = []
for i in range(T) :
    N = int(input())
    dfs(0)
    if i != T - 1 :
        print()