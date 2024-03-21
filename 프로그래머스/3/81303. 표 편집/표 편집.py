def solution(n, k, cmd):
    answer = ''
    linked = {}
    
    for i in range(n) :
        if i == 0 :
            linked[i] = [None, i + 1]
        elif i == n - 1 :
            linked[i] = [i - 1, None]
        else :
            linked[i] = [i - 1, i + 1]
    
    pointer = k
    trash = []
    for i in cmd :
        c = i.split(" ")
        if c[0] == 'U' :
            for _ in range(int(c[1])) :
                if linked[pointer][0] == None :
                    break
                pointer = linked[pointer][0]
                
                
        elif c[0] == 'D' :
            for _ in range(int(c[1])) :
                if linked[pointer][1] == None :
                    break
                pointer = linked[pointer][1]
                
        elif c[0] == 'C' :
            left, right = linked[pointer][0], linked[pointer][1]
            if left == None :
                linked[right][0] = None
            elif right == None :
                linked[left][1] = None
            else :
                linked[left][1] = right
                linked[right][0] = left
            trash.append([pointer, left, right])
            
            if right != None :
                pointer = right
            else :
                pointer = left
                
        elif c[0] == 'Z' :
            temp, left, right = trash.pop()
            if left == None :
                linked[right][0] = temp
            elif right == None :
                linked[left][1] = temp
            else :
                linked[left][1] = temp
                linked[right][0] = temp

    trash_dict = {}
    for i in trash :
        trash_dict[i[0]] = i[0]
    
    for i in range(n) :
        if i in trash_dict :
            answer += 'X'
        else :
            answer += 'O'

    return answer