def solution(msg):
    answer = []
    dict_word = {}
    
    for i in range(1, 27) :
        dict_word[chr(64 + i)] = i
    
    dict_val = 27
    s = ''
    for i in range(len(msg)) :
        w = msg[i]
        if len(s) > i :
            continue
        for j in range(i + 1, len(msg)) :
            c = msg[j]
            if w + c in dict_word :
                w += c
            else :
                dict_word[w + c] = dict_val
                dict_val += 1
                break
        s += w
        answer.append(dict_word[w])

    return answer