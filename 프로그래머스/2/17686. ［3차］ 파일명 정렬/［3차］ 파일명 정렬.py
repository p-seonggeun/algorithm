def solution(files):
    answer = []
    temp = []
    for i in files :
        head = ''
        number = ''
        tail = ''
        h_index, n_index, t_index = 0, 0, 0
        
        for index, j in enumerate(i) :
            if j.isdigit() :
                h_index = index
                break
        
        head = i[:h_index]
        
        for j in range(h_index, len(i)) :
            if not i[j].isdigit() :
                n_index = j
                break
        
        if n_index == 0 :
            n_index = len(i)

        number = i[h_index:n_index]
        
        if len(head + number) == len(i) :
            tail = ''
        else :
            tail = i[n_index:]
            
        temp.append([head, number, tail, i])
    
    temp = sorted(temp, key = lambda x : (x[0].lower(), int(x[1])))
        
    for i in temp :
        answer.append(i[-1])
        
    return answer