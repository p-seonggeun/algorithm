def solution(m, musicinfos):
    answer = ''
    temp = []
    dictionary = {'C#' : 'Q', 'D#' : 'W', 'F#' : 'U', 'G#' : 'R', 'A#' : 'T', 'B#' : 'Y'}
    def time(start, end) :
        start_h, start_m = map(int, start.split(":"))
        end_h, end_m = map(int, end.split(":"))
        total_h = end_h - start_h
        total_m = end_m - start_m
        if total_m < 0 :
            total_h -= 1
            total_m += 60
        return (total_h * 60) + total_m
    
    def play(total, music) :
        ret = ''
        if total < len(music) :
            return music[:total]
        else :
            repeat = total // len(music)
            total = total % len(music)
            ret = music * repeat
            ret += music[:total]
        return ret
    
    for i in musicinfos :
        l = i.split(",")
        start, end, title, music = l[0], l[1], l[2], l[3]
        total_time = time(start, end)
        for i in dictionary.keys() :
            if i in music :
                music = music.replace(i, dictionary[i])
        music = play(total_time, music)
        
        for i in dictionary.keys() :
            if i in m :
                m = m.replace(i, dictionary[i])
        
        if m in music :
            temp.append([total_time, title])  
    
    if len(temp) == 0 :
        return "(None)"
    else :
        temp.sort(key = lambda x : (-x[0]))
    
    answer = temp[0][1]
        
    return answer