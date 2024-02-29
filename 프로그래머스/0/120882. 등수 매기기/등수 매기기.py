def solution(score):
    answer = []
    average = []
    dict_score = {}
    for i in range(len(score)) :
        average.append(score[i][0] + score[i][1])
    average.sort(reverse = True)
    for index, i in enumerate(average) :
        if i not in dict_score :
            dict_score[i] = index + 1
    
    for i in score :
        answer.append(dict_score[sum(i)])
    
    return answer