def solution(record):
    answer = []
    dictionary = {}
    
    for i in record :
        command = i.split(" ")
        if len(command) == 3 :
            operate, uid, nickname = command[0], command[1], command[2]
            if operate == 'Enter' :
                if uid in dictionary :
                    dictionary[uid] = nickname
                else :
                    dictionary[uid] = nickname
                sql = uid + "님이 들어왔습니다."
                answer.append(sql)
            else :
                dictionary[uid] = nickname
        else :
            operate, uid = command[0], command[1]
            sql = uid + "님이 나갔습니다."
            answer.append(sql)
    
    for i in range(len(answer)) :
        uid_index = answer[i].index("님")
        answer[i] = dictionary[answer[i][:uid_index]] + answer[i][uid_index:]
        
    return answer