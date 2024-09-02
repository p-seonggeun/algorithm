def solution(skill, skill_trees):
    answer = 0
    skill = list(skill[::-1])
    
    for i in skill_trees :
        a = list(i[::-1])
        b = skill[::]
        flag = True
        while a :
            t = a.pop()
            if t in b :
                if b.pop() != t :
                    flag = False
                    break
        if flag :
            answer += 1
                    
    return answer