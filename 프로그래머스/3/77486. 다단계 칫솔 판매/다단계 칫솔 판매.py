def solution(enroll, referral, seller, amount) :
    answer = []
    dict = {}
    d = {"-" : 0}
    for i in enroll :
        if i not in d :
            d[i] = 0
            
    for i, j in zip(enroll, referral) :
        dict[i] = j
    
    amount = [i * 100 for i in amount]
    
    for i, j in zip(seller, amount) :
        key, value = i, j
        temp = 0
        while key != '-':
            if value == 0 :
                break
            next_value = int(value * 0.1)
            current_value = value - next_value
            value = next_value
            d[key] += current_value
            key = dict[key]
            if key == '-' :
                d[key] += value
    
    
    for i, j in d.items() :
        if i != '-' :
            answer.append(j)
    
    return answer