def solution(skill, skill_trees):
    answer = 0
    def check(s1, s2) :
        for i, j in zip(s1, s2) :
            if i != j :
                return False
        return True
    
    for i in skill_trees :
        temp = []
        l = list(i)
        while l :
            t = l.pop()
            if t in skill :
                temp.append(t)
        
        temp = ''.join(temp[::-1])
        
        if check(temp, skill) :
            answer += 1
    return answer