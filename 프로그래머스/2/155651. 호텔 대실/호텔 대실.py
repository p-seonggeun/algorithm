def solution(book_time):
    answer = 0
    l = [0] * 3500
    for i in book_time :
        s, e = i
        
        s, e = int(''.join(s.split(":"))), int(''.join(e.split(":")))
        print(e)
        if int(str(e)[-2] + str(e)[-1]) + 10 >= 60 :
            e += 40
            
        for j in range(s, e + 10) :
            l[j] += 1
    answer = max(l)
    return answer