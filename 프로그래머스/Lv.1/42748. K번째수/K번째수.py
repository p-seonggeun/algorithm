def solution(array, commands):
    answer = []
    for l in commands :
        i = l[0]
        j = l[1]
        k = l[2]
        
        print(array[i-1:j])
        
        temp = array[i-1:j]
        temp.sort()
        temp = temp[k - 1]
        
        answer.append(temp)
    return answer