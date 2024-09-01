def solution(msg):
    answer = []
    d = {}
    for i in range(65, 91) :
        d[chr(i)] = i - 64
    val = 27
    
    while msg != '' :
        w = ''
        for i in range(len(msg)) :
            if w + msg[i] in d :
                w += msg[i]
            else :
                answer.append(d[w])
                d[w + msg[i]] = val
                val += 1
                msg = msg[len(w):]
                break
        else :
            answer.append(d[w])
            break
    return answer