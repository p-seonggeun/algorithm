def solution(my_string, m, c):
    answer = ''
    l = [[] for _ in range(m)]
    
    for i in range(len(my_string)) :
        l[i % m].append(my_string[i])
    
    answer = ''.join(l[c - 1])
            
    return answer