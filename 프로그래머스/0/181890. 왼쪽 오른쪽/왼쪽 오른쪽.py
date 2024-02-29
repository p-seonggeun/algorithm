def solution(str_list):
    answer = []
    split_index = -1
    split_vector = ''
    for index, i in enumerate(str_list) :
        if i == "l" or i == "r" :
            split_index = index
            split_vector = i
            break
    
    if split_index == -1 :
        return answer
    else :
        if split_vector == 'l' :
            return str_list[:split_index]
        elif split_vector == 'r' :
            return str_list[split_index + 1:]