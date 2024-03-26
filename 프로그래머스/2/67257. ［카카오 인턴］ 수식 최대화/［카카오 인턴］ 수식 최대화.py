from itertools import permutations
def solution(expression):
    answer = 0
    
    def dfs(exp, depth) :
        if exp.isdigit() :
            return int(exp)
        temp = []
        l = exp.split(op[depth])
        for i in l :
            temp.append(str(dfs(i, depth + 1)))
        return eval(op[depth].join(temp))
    
    
    for op in list(permutations(("*", "-", "+"))) :
        answer = max(answer, abs(dfs(expression, 0)))
            
    return answer