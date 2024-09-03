def solution(record):
    answer = []
    d = {}    
    
    for i in record :
        t = i.split(" ")
        if t[0] == "Enter" :
            d[t[1]] = t[2]
        elif t[0] == 'Change' :
            d[t[1]] = t[2]
    
    for i in record :
        t = i.split(" ")
        if t[0] == "Enter" :
            answer.append(d[t[1]] + "님이 들어왔습니다.")
        elif t[0] == "Leave" :
            answer.append(d[t[1]] + "님이 나갔습니다.")
    
    return answer