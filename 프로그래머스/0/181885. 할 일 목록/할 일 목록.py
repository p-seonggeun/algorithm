def solution(todo_list, finished):
    answer = []
    for i, j in zip(todo_list, finished) :
        if j :
            continue
        else :
            answer.append(i)
    return answer