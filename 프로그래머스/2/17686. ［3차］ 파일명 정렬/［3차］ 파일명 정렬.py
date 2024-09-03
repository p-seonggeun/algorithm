def solution(files):
    answer = []
    l = []
    
    for i in files :
        h, n, t = '', '', ''
        index = 0
        while not (i[index].isnumeric()) :
            h += i[index]
            index += 1
        
        while len(n) <= 5 and i[index].isnumeric() :
            n += i[index]
            index += 1
            if index == len(i) :
                break
        else :
            t = i[index:]
        
        
        l.append([h, n, t])
    
    l.sort(key = lambda x : (x[0].lower(), int(x[1])))
    
    for i in l :
        answer.append(''.join(i))
                
    
    return answer